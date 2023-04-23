import numpy as np
import pandas as pd
from flask import Flask, render_template, request,jsonify
import csv
import pickle
import sklearn
from sklearn.compose import make_column_transformer
import joblib

app = Flask(__name__)
data = pd.read_csv('CLEANED_DATA.csv')
# with open('Lassomodel.pk1','rb') as f:
#     pipe=pickle.load(f)
pipe = pickle.load(open("Lassomodel (3).pk1",'rb'))

@app.route('/')
def index():

    locations = sorted(data['Address'].unique())
   
   
    return render_template('index.html',locations=locations) 

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bed = request.form.get('bedrooms')
    bath = request.form.get('Bathrooms')
    sqft = request.form.get('squarefeet')
    new = request.form.get('neworold')
    type = request.form.get('typeofb')
    
    if new == 'Resale':
        new=0
    else:
        new=1

    if type == 'Flat':
        type=0
    else:
        type=1

    if location == 'other':
        location=4343
    elif location == 'Mira Road, Mumbai - Mira Road and Beyond, Maharashtra':
        location=154
    elif location == 'Andheri West, Mumbai - Western Suburbs, Maharashtra':
        location=129
    elif location == 'Andheri East, Mumbai - Western Suburbs, Maharashtra':
        location=81
    elif location == 'Chembur, Mumbai - Harbour Line, Maharashtra':
        location=79
    elif location == 'Mulund West, Mumbai - Central Line, Maharashtra':
        location=78
    elif location == 'Kandivali West, Mumbai - North Mumbai, Maharashtra':
        location=70
    elif location == 'Malad West, Mumbai - Western Suburbs, Maharashtra':
        location=69
    elif location == 'Borivali West, Mumbai - Western Suburbs, Maharashtra':
        location=64
    elif location == 'Virar West, Mumbai - Mira Road and Beyond, Maharashtra':
        location=60
    elif location == 'Kandivali East, Mumbai - North Mumbai, Maharashtra':
        location=52
    elif location == 'Goregaon West, Mumbai - North Mumbai, Maharashtra':
        location=44
    elif location == 'Goregaon East, Mumbai - Western Suburbs, Maharashtra':
        location=41
    elif location == 'Ghatkopar West, Mumbai - Central Line, Maharashtra':
        location=40
    elif location == 'Bhandup West, Mumbai - Central Line, Maharashtra':
        location=38
    elif location == 'Malad East, Mumbai - North Mumbai, Maharashtra':
        location=35
    elif location == 'Borivali East, Mumbai - Western Suburbs, Maharashtra':
        location=33
    elif location == 'Powai, Mumbai - Central Line, Maharashtra':
        location=33
    elif location == 'Dahisar East, Mumbai - North Mumbai, Maharashtra':
        location=32
    elif location == 'Santacruz West, Mumbai - Western Suburbs, Maharashtra':
        location=31
    elif location == 'Vile Parle East, Mumbai - Western Suburbs, Maharashtra':
        location=30
    elif location == 'Kalyan, Mumbai - Around Mumbai, Maharashtra':
        location=30
    elif location == 'Virar, Mumbai - Mira Road and Beyond, Maharashtra':
        location=27
    elif location == 'Parel, Mumbai - South Mumbai, Maharashtra':
        location=26
    elif location == 'Mulund East, Mumbai - Central Line, Maharashtra':
        location=26
    elif location == 'Ulhasnagar, Mumbai - Around Mumbai, Maharashtra':
        location=25
    elif location == 'Worli, Mumbai - South Mumbai, Maharashtra':
        location=24
    elif location == 'Vasai East, Mumbai - Mira Road and Beyond, Maharashtra':
        location=24
    elif location == 'Mira Road, Mumbai, Mira Road, Mumbai - Mira Road and Beyond, Maharashtra':
        location=23
    elif location == 'Vasai West, Mumbai - Mira Road and Beyond, Maharashtra':
        location=22
    elif location == 'Santacruz East, Mumbai - Western Suburbs, Maharashtra':
        location=21
    elif location == 'Bandra West, Mumbai - Western Suburbs, Maharashtra':
        location=21
    elif location == 'Marol, Mumbai - Western Suburbs, Maharashtra':
        location=21
    elif location == 'Vasai, Mumbai - Mira Road and Beyond, Maharashtra':
        location=21
    elif location == 'Juhu, Mumbai - Western Suburbs, Maharashtra':
        location=19
    elif location == 'Worli, Mumbai, Worli, Mumbai - South Mumbai, Maharashtra':
        location=19
    elif location == 'Chandivali, Mumbai - Central Line, Maharashtra':
        location=18
    elif location == 'Mulund West, Mumbai, Mulund West, Mumbai - Central Line, Maharashtra':
        location=18
    elif location == 'Khar West, Mumbai - Western Suburbs, Maharashtra':
        location=18
    elif location == 'Bhayandar West, Mumbai - Mira Road and Beyond, Maharashtra':
        location=17
    elif location == 'Mira Bhayandar, Mumbai - Mira Road and Beyond, Maharashtra':
        location=16
    elif location == 'Prabhadevi, Mumbai - South Mumbai, Maharashtra':
        location=15
    elif location == 'hane-Kalyan-Dombivli, Mumbai, Maharashtra':
        location=15
    elif location == 'Tilak Nagar - Harbour Line, Mumbai - Harbour Line, Maharashtra':
        location=15
    elif location == 'Vile Parle West, Mumbai - Western Suburbs, Maharashtra':
        location=15
    elif location == 'Sion, Mumbai - Central Mumbai, Maharashtra':
        location=14
    elif location == 'Lokhandwala Complex, Mumbai - Western Suburbs, Maharashtra':
        location=13
    elif location == 'Ambernath, Mumbai, Maharashtra':
        location=13
    elif location == 'Thane, Mumbai, Maharashtra':
        location=12
    elif location == 'Kanjurmarg East, Mumbai - Central Line, Maharashtra':
        location=12
    elif location == 'Bhayandar East, Mumbai - Mira Road and Beyond, Maharashtra':
        location=12
    elif location == 'Goregaon East, Mumbai, Goregaon East, Mumbai - Western Suburbs, Maharashtra':
        location=12
    elif location == 'Malad West, Mumbai, Malad West, Mumbai - Western Suburbs, Maharashtra':
        location=11
    elif location == 'Mahim West, Mumbai - Central Mumbai, Maharashtra':
        location=11
    elif location == 'Kandivali East, Mumbai, Thakur Village, Mumbai - North Mumbai, Maharashtra':
        location=11
    elif location == 'Bandra East, Mumbai - Western Suburbs, Maharashtra':
        location=11
    elif location == 'Oshiwara, Mumbai - Western Suburbs, Maharashtra':
        location=11
    elif location == 'Charkop, Mumbai - North Mumbai, Maharashtra':
        location=11
    elif location == 'Andheri East, Mumbai, Andheri East, Mumbai - Western Suburbs, Maharashtra':
        location=11
        
    
    

        
    
    
  
  
    

    # print(location, bed, bath, sqft,)
    input = pd.DataFrame([[sqft,bath,bed,new,type,location]],columns=[ 'area', 'Bathrooms', 'Bedrooms','neworold','type_of_building','Address'])
    print(pipe.predict(input))
    prediction = pipe.predict(input)[0]
    

    return str(np.round(prediction,4))
    # return str(prediction)
    
    #for avtivating virtual Environment type below code
    # .\env\Scripts\activate.ps1
   
if __name__=="__main__":
    app.run(debug=True, port=5001)