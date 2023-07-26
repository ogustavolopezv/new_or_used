from fastapi import APIRouter
from machine_learning.schemas.new_or_used_v9 import NewOrUsed, NewOrUsedPredictionResponse, format_response_data
import pandas as pd
import machine_learning.classifier as clf

app_new_or_used_predict_v9 = APIRouter()


@app_new_or_used_predict_v9.post('/new_or_used/predict',
                                 tags=["Predictions"],
                                 response_model=NewOrUsedPredictionResponse,
                                 description="Get a classification for New or Used")
async def get_prediction(new_or_used: NewOrUsed):
    data = dict(new_or_used)['data']
    data_formatted = format_response_data(data)
    prediction = clf.model.predict(data_formatted).tolist()
    probability = clf.model.predict_proba(data_formatted).tolist()
    log_probability = clf.model.predict_log_proba(data_formatted).tolist()
    return {"prediction": prediction,
            "probability": probability,
            "log_probability": log_probability}