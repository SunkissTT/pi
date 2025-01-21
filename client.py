from flask import Flask, render_template, jsonify, request, send_file
import subprocess
import json
import datetime
import os
import time
from threading import Thread

app = Flask(__name__)
test_process = None
filename = None  # Make filename global

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_test', methods=['POST'])
def start_test():
    global test_process, filename
    server_ip = '10.10.0.1'
    port = 11111
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'iperf3_log_{timestamp}.json'

    cmd = f"iperf3 -c {server_ip} -p {port} -i 5 -t 30 --json > {filename}"
    test_process = subprocess.Popen(cmd, shell=True)

    return jsonify({'message': 'Test started', 'filename': filename})

@app.route('/stop_test', methods=['POST'])
def stop_test():
    global test_process, filename

    def remove_file():
        time.sleep(10)  # 10초 후 파일 삭제
        if os.path.exists(filename):
            os.remove(filename)
    
    if test_process is not None:
        test_process.terminate()
        test_process = None
        # 파일 삭제 스레드 시작
        thread = Thread(target=remove_file)
        thread.start()
        
        return jsonify({'message': 'Test stopped'})
    else:
        return jsonify({'message': 'No test is currently running'})

@app.route('/get_log/<filename>', methods=['GET'])
def get_log(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
