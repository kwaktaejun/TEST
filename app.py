from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask!"

@app.route('/upload_excel_notion')
def upload_excel_notion():
    return render_template('upload_excel_notion.html')

if __name__ == '__main__':
    app.run()