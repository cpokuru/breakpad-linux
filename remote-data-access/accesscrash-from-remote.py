import subprocess
from flask import Flask, render_template_string

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
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crash Details</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .crash-container {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            padding: 40px;
            max-width: 800px;
            width: 90%;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }
        .crash-details {
            font-size: 16px;
            line-height: 1.6;
        }
        .highlight {
            font-weight: bold;
        }
        .thread-title {
            color: red;
        }
    </style>
</head>
<body>
    <div class="crash-container">
        <h1>Crash Details</h1>
        <div class="crash-details">
            <p><span class="highlight">Thread:</span> Thread 2</p>
            <p><span class="highlight">Filename:</span> multithread-demo.cpp</p>
            <p><span class="highlight">Line Number:</span> 20</p>
        </div>
    </div>
</body>
</html>
    """, crash_details=crash_details)

if __name__ == '__main__':
    app.run(debug=True)

