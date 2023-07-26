import machine_learning.classifier as clf
from fastapi import FastAPI
from joblib import load
from routes.v9.new_or_used_predict import app_new_or_used_predict_v9
from routes.home import app_home


app = FastAPI(title="MELI New or Used Model Classifier API",
              description="API for classifier model New or Used", version="9.0")


@app.on_event('startup')
async def load_model():
    clf.model = load('machine_learning/models/new_or_used_v9.joblib')


app.include_router(app_home)
app.include_router(app_new_or_used_predict_v9, prefix='/v9')
