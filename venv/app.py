import flask
import numpy as np
from flask import Flask, redirect, url_for, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("../model/model.pkl", "rb"))

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 2)
    loaded_model = pickle.load(
        open(model))  # load the model
    # predict the values using loded model
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/hasil' , methods = ['POST', 'GET'])
def hasil():
    if request.method == 'POST':
        nama = request.form['name']
        sunshine = request.form['sunshine-hour']
        work = request.form['work-hour']

        text = nama + ", your city have " + sunshine + " hours of sunshine per day and " + work + " hours of work per day will make you happy."

        to_predict_list = list(map(float, [sunshine, work]))
        result = ValuePredictor(to_predict_list)
        if int(result) == 2:
            prediction = text + '\nSo your city have a healthy lifestyle'
        elif int(result) == 1:
            prediction = text + '\nSo your city have a normal lifestyle'
        else:
            prediction = text + '\nSo your city have a bad lifestyle'

        return flask.render_template("index.html", prediction=prediction)
if __name__ == "__main__":
    app.run(debug=False)  # use debug = False for jupyter notebook