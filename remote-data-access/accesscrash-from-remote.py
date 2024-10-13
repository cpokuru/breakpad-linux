import subprocess
from flask import Flask, render_template

app = Flask(__name__)

def run_decode_crash():
    try:
        # Execute decodecrash and capture its output
        process = subprocess.Popen(['./decodecrash'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, _ = process.communicate()
        return output
    except Exception as e:
        return f"Error executing decodecrash: {e}"

def extract_crash_details(output):
    crash_details = ""
    thread_info = ""
    filename = ""
    line_number = ""
    lines = output.split('\n')
    for line in lines:
        if "crashed" in line:
            thread_info = line.split(" (")[0].split()[-1]  # Extract thread number
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
    # Run decodecrash and get the output
    output = run_decode_crash()
    
    # Extract crash details from the output
    crash_details = extract_crash_details(output)
    
    # Pass the crash details to the template
    return render_template('index.html', crash_details=crash_details)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, host='192.168.64.26', port=8084)
