from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-trans-box', methods=['POST'])
def run_trans_box():
    user_input = request.form['user_input']
    # trans_box.py에 사용자 입력 전달 및 실행 결과 캡처
    result = subprocess.run(['python', 'trans_box.py', user_input], capture_output=True, text=True)
    return result.stdout

@app.route('/run-ai-box', methods=['POST'])
def run_ai_box():
    user_input = request.form['user_input']
    # ai_box.py에 사용자 입력 전달 및 실행 결과 캡처
    result = subprocess.run(['python', 'ai_box.py', user_input], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
