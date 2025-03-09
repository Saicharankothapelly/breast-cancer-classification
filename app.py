import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
#Loas the pickle model
model = pickle.load(open('bc_model.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/classify_api',methods=['POST'])
def classify_api():
    data = request.json['data']
    new_data = np.array(list(data.values())).reshape(1,-1)
    output = model.predict(new_data)
    output_int = int(output[0])  # Convert int64 to int
    return jsonify(output_int)

@app.route('/classify',methods=['POST'])
def classify():
    data= [float(x) for x in request.form.values()]
    new_data = np.array(data).reshape(1,-1)
    output=model.predict(new_data)
    output_int = int(output[0])
    prediction_text = f"The type of breast cancer is {'Malignant' if output_int == 1 else 'Benign'}"

    return render_template("home.html", prediction_text=prediction_text)
    
    
if __name__ =="__main__":
    app.run(debug=True)