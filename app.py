from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import os
import io

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(debug=True)