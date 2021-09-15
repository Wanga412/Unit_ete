from flask import Flask, render_template, request, json
from main import *
import json
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', value=data)


@app.route('/getValue', methods= ['POST'])
def dab():
    global data
    data = request.form
    data = dict(data.lists())
    print(data)
    return ""

app.run()