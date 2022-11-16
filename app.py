import flask
from flask import Flask,redirect, url_for, request, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hasil' , methods = ['POST', 'GET'])
def hasil():
    return render_template('hasil.html')