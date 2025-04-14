from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/upload_excel_notion', methods=['GET', 'POST'])
def upload_excel_notion():
    if request.method == 'POST':
        # 파일 처리 로직은 생략
        return '업로드 완료'
    return render_template('upload_excel_notion.html')

if __name__ == '__main__':
    app.run()
