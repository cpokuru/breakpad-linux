import subprocess
from flask import Flask

app = Flask(__name__)

def run_decode_crash():
    process = subprocess.Popen(['./decodecrash'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = process.communicate()
    return output

def extract_crash_details(output):
    crash_details = ""
    enter_flag = False
    lines = output.split('\n')
    for line in lines:
        if not enter_flag and "crashed" in line:
            crash_details += "ENter --\n" + line + "\n"
            enter_flag = True
        elif enter_flag:
            crash_details += line + "\n"
            if "EXit --" in line:
                break
    return crash_details

@app.route('/')
def index():
    output = run_decode_crash()
    crash_details = extract_crash_details(output)
    return f"<pre>{crash_details}</pre>"

if __name__ == '__main__':
    app.run(debug=True)

