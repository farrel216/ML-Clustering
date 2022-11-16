import flask
from flask import Flask,redirect, url_for, request, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hasil' , methods = ['POST', 'GET'])
def hasil():
    if request.method == 'POST':
        nama = request.form['name']
        sunshine = request.form['sunshine-hour']
        work = request.form['work-hour']
        result = "Hello " + nama + " , " + sunshine + " hours of sunshine per day and " + work + " hours of work per day will make you happy."
        return render_template("index.html",result=result)
