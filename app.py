import pandas as pd
from flask import Flask, render_template, url_for, request, session, redirect,flash
from flaskwebgui import FlaskUI
from flask_socketio import SocketIO
from datetime import date, timedelta
import json
import time 

app = Flask(__name__)


@app.route('/', methods = ["GET","POST"]) 
def home():
    if request.method=='POST':   

        try:
            file= request.files['file'] 
            df = pd.read_excel(file)   
            df.to_excel('Ads Data.xlsx') 

        except ValueError:
            return render_template('demo.html')  

    return render_template('demo.html')  

@app.route('/demo')
def demo(): 

    df=pd.read_excel('Ads Data.xlsx') 
    data={'Sales' : df['Sales'].tolist(),
            'Spend' : df['Spend'].tolist(),
            'Month' : df['Month'].tolist()
            } 
    
    return json.dumps(data)

@app.route('/pie')
def pie(): 

    df=pd.read_excel('Ads Data.xlsx')  
    df['perc']= round((df['Total sales']/ df['Total sales'].sum())*100, 2) 
    df=df[['Month','perc']]  
    df= df.rename(columns={'Month':'name','perc':'y'})  
    d=df.to_dict('records')  
    
    return json.dumps(d)  

@app.route('/atos')
def atos():  

    df=pd.read_excel('Ads Data.xlsx') 
    df= df.round(2) 

    data={'ACOS' : df['ACOS'].tolist(),
            'TACOS' : df['TACOS'].tolist(), 
            'Month' : df['Month'].tolist()
            } 
        
    return json.dumps(data)   


@app.route('/all')
def all():  

    df=pd.read_excel('Ads Data.xlsx') 
    df= df.round(2) 

    data={'ACOS' : df['ACOS'].tolist(),
            'TACOS' : df['TACOS'].tolist(),       
            'Sales' : df['Sales'].tolist(), 
            'Spend' : df['Spend'].tolist(), 
            'Month' : df['Month'].tolist(), 
            } 
        
    return json.dumps(data)   


if __name__ == '__main__':
    app.run(debug=True) 
