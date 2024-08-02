import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

# Creating basic Flask Application
app = Flask(__name__)

# Loading model
model = pickle.load(open('Linear_Regression_Model.pkl','rb'))
reg_sc = pickle.load(open('Linear_Regression_sc_Model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    data2 = np.array(list(data.values())).reshape(1,-1)
    print(data2)
    new_data = reg_sc.transform(data2)

    output = model.predict(new_data)
    print("Predicted Output",output[0])
    return jsonify(output[0])


@app.route('/predict',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    sc_data = reg_sc.transform(np.array(data).reshape(1,-1))
    output = model.predict(sc_data)[0]

    return render_template("home.html",prediction_text = "The preidcted House Price is:{}".format(output))

if __name__ == "__main__":
    app.run(debug=True)
