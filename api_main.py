from fastapi import FastAPI
from pydantic import BaseModel,Field
import joblib
import pandas as pd
import json

# Load the trained pipeline
model = joblib.load("models/xgb_pipeline.pkl")

app = FastAPI(title="Bank Marketing Prediction API")

# Define the input schema using Pydantic
class BankClient(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    contact: str
    month: str
    day_of_week: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str
    euribor3m: float

    emp_var_rate: float = Field(..., alias="emp.var.rate")
    cons_price_idx: float = Field(..., alias="cons.price.idx")
    cons_conf_idx: float = Field(..., alias="cons.conf.idx")
    
    nr_employed: float = Field(..., alias="nr.employed")
    class Config:
        populate_by_name = True  # So aliases work during input
        json_schema_extra = {
            "example": {
                "age": 35,
                "job": "technician",
                "marital": "married",
                "education": "secondary",
                "default": "no",
                "housing": "yes",
                "loan": "no",
                "contact": "cellular",
                "month": "may",
                "day_of_week": "mon",
                "duration": 210,
                "campaign": 2,
                "pdays": 999,
                "previous": 0,
                "poutcome": "nonexistent",
                "emp.var.rate": 1.1,
                "cons.price.idx": 93.994,
                "cons.conf.idx": -36.4,
                "euribor3m": 4.857,
                "nr.employed": 5191.0
            }
        }
    

@app.get("/")
def home():
    return {"message": "🏦 Bank Marketing API is running!"}

@app.post("/predict")
def predict(client: BankClient):
    input_df = pd.DataFrame([client.model_dump(by_alias=True)])

    prob = model.predict_proba(input_df)[0][1]
    prediction = int(prob >= 0.4)
    return {
        "prediction": int(prediction),
        "probability": round(float(prob), 4),
        "subscribed": "yes" if prediction == 1 else "no"
    }
