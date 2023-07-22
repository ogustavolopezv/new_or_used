import models.ml.classifier as clf
from fastapi import FastAPI
from joblib import load
from routes.v1.new_or_used_predict import app_new_or_used_predict_v1
from routes.home import app_home


app = FastAPI(title="MELI New or Used Model Classifier API",
              description="API for classifier model New or Used", version="1.0")


@app.on_event('startup')
async def load_model():
    clf.model = load('models/ml/new_or_used_v1.joblib')


app.include_router(app_home)
app.include_router(app_new_or_used_predict_v1, prefix='/v1')
