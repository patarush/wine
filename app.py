# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:55:56 2020

@author: hp
"""

from flask import Flask , request
import pandas as pd
import numpy  as np
import pickle
import flasgger
from flasgger import Swagger

app= Flask(__name__)
Swagger(app)

pickle_in=open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome"

@app.route('/predict',methods=["Get"])
def pred_wine_type():

    """Lets Predict Wine type  
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Alcohol
        in: query
        type: number
        required: true
      - name: Malic
        in: query
        type: number
        required: true
      - name: Ash 
        in: query
        type: number
        required: true
      - name: Alcalinity
        in: query
        type: number
        required: true
      - name: Magnesium
        in: query
        type: number
        required: true
      - name: Phenols
        in: query
        type: number
        required: true
      - name: Flavanoids
        in: query
        type: number
        required: true
      - name: Nonflavanoids
        in: query
        type: number
        required: true
      - name: Proanthocyanins
        in: query
        type: number
        required: true
      - name: Color
        in: query
        type: number
        required: true
      - name: Hue
        in: query
        type: number
        required: true
      - name: Dilution
        in: query
        type: number
        required: true
      - name: Proline
        in: query
        type: number
        required: true
    responses:
        200:
            description: Output
        
            
    """
  
    Alcohol	=request.args.get('Alcohol')
    Malic=request.args.get('Malic')
    Ash=request.args.get('Ash')
    Alcalinity=request.args.get('Alcalinity')
    Magnesium=request.args.get('Magnesium')
    Phenols=request.args.get('Phenols')
    Flavanoids=request.args.get('Flavanoids')
    Nonflavanoids=request.args.get('Nonflavanoids')
    Proanthocyanins=request.args.get('Proanthocyanins')
    Color=request.args.get('Color')
    Hue=request.args.get('Hue')
    Dilution=request.args.get('Dilution')
    Proline=request.args.get('Proline')
    prediction=classifier.predict([[Alcohol,Malic,Ash,Alcalinity,Magnesium,Phenols,Flavanoids,Nonflavanoids,Proanthocyanins,Color,Hue,Dilution,Proline]])
    return 'The predicted value is'+str(prediction)
    
if __name__=='__main__':
    app.run(debug=TRUE)
    
#host="0.0.0.0",port=5000