from fastapi import APIRouter
from models.schemas.new_or_used import NewOrUsed, NewOrUsedPredictionResponse
import models.ml.classifier as clf

app_new_or_used_predict_v1 = APIRouter()


@app_new_or_used_predict_v1.post('/new_or_used/predict',
                                 tags=["Predictions"],
                                 response_model=NewOrUsedPredictionResponse,
                                 description="Get a classification for New or Used")
async def get_prediction(new_or_used: NewOrUsed):
    data = dict(new_or_used)['data']
    prediction = clf.model.predict(data).tolist()
    return {"prediction": prediction}
