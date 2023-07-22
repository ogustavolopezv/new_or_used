from fastapi import APIRouter
app_home = APIRouter()


@app_home.get('/', tags=["Intro"])
async def hello():
    return {"message": "Hola!"}


@app_home.get('/bye', tags=["Intro"])
async def bye():
    return {"message": "Adiós!"}
