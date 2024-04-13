from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle
import json


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3002"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class CreditRating(BaseModel):
    chk_acct: int
    duration: int
    history: int
    purpose_of_credit: int
    credit_amount: int
    balance: int
    employment: int
    install_rate: int
    marital_status: int
    real_estate: int
    age: int
    other_installment: int
    num_credits: int
    job: int
    phone: int
    foreign: int


# loading model 
prediction_model = pickle.load(open('classifier.sav','rb'))

@app.get('/')
def welcome():
    return "hey welcome to this page"

@app.post('/predict')
def credit_prediction(input_parameters: CreditRating):
    input_data = input_parameters.dict()
    input_list = [input_data[field] for field in input_data]
    
    prediction = prediction_model.predict([input_list])

    if prediction[0] == 0:
        return "The credit card rating is bad."
    else:
        return "The credit card rating is good."