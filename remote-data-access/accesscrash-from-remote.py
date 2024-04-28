import subprocess
from flask import Flask

app = Flask(__name__)

def run_decode_crash():
    process = subprocess.Popen(['./decodecrash'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = process.communicate()
    return output

def extract_crash_details(output):
    crash_details = ""
    thread_info = ""
    filename = ""
    line_number = ""
    lines = output.split('\n')
    for line in lines:
        if "crashed" in line:
            thread_info = line.split(" (")[0]  # Extract thread number
        elif "EXit --" in line:
            crash_details += f"crashed happened in thread: {thread_info}\n"
            crash_details += f"filename: {filename}\n"
            crash_details += f"line number: {line_number}\n"
            break
        elif ".cpp" in line:
            parts = line.split(":")
            filename = parts[0].split("[")[-1].strip()  # Extract filename without extra characters
            line_number = parts[1].split(" ")[1]
        elif thread_info:
            crash_details += line + "\n"
    return crash_details

@app.route('/')
def index():
    output = run_decode_crash()
    crash_details = extract_crash_details(output)
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .crash-details {{
                margin-top: 20px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }}
            .thread-title {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <div class="crash-details">
            <pre>{crash_details}</pre>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
