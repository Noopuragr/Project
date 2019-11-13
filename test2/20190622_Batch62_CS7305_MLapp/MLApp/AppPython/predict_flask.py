from flask import Flask, request, Response, render_template
import os
from joblib import load
from werkzeug import secure_filename
import pandas as pd

app = Flask(__name__)
PATH = os.getcwd()

def load_Model():
  clf = load(PATH + '/pickle/model.pkl')
  return clf

model = load_Model()

@app.route('/')
def index():
  return render_template('welcome.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    name = request.values.get('firstname')
    number = request.values.get('number')
    # creating list        
    output_result = []  

    def __init__(self, name, number):  
        self.name = name  
        self.number = number 

    if number < 1:
      number = 1

    for x in range(number):
      output_result.append( geeks(name, x) ) 

    return render_template('value.html', output_result = output_result)

if __name__=="__main__":
    app.run(host="127.0.0.1", port=1234, debug=True)