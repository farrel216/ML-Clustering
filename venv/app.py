import flask
import numpy as np
from flask import Flask, redirect, url_for, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 3)
    loaded_model = pickle.load(
        open("./model/model.pkl", "rb"))  # load the model
    # predict the values using loded model
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/hasil' , methods = ['POST', 'GET'])
def hasil():
    if request.method == 'POST':
        nama = request.form['name']
        sleep = request.form['sleeping-hours']
        heart = request.form['avg-hr']
        resp = request.form['avg-rs']

        # text = nama + ", your city have " + sunshine + " hours of sunshine per day and " + work + " hours of work per day will make you happy."

        to_predict_list = list(map(float, [sleep, heart, resp]))
        result = ValuePredictor(to_predict_list)
        if int(result) == 1:
            prediction = nama + ', stress level kamu <b>rendah</b>. Bagus, kamu bisa bekerja dengan tenang dan produktif. Tetap semangat ya!'
        elif int(result) == 2:
            prediction = nama + ', stress level kamu <b>medium</b>. Kamu bisa tetap produktif dan tenang, tapi jangan lupa untuk mengambil waktu untuk diri sendiri.'
        else:
            prediction = nama + ', stress level kamu <b>tinggi</b>. Kamu harus lebih berhati-hati dalam menjalani kehidupan sehari-hari. Jangan lupa untuk mengambil waktu untuk diri sendiri.'

        return prediction
if __name__ == "__main__":
    app.run(debug=False)  # use debug = False for jupyter notebook