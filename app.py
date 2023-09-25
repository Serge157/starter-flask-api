from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = "Serhii Buza"
    return  render_template('index.html', name=name)
