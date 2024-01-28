from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Create a separate process for running stress_cpu.py
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return 'Stress CPU process started.'

    elif request.method == 'GET':
        # Return the private IP address of the EC2 instance
        private_ip = socket.gethostbyname(socket.gethostname())
        return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
