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
    
if __name__ =="__main__":
    app.run(debug=True)