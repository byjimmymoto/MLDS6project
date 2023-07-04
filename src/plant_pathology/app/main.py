import uvicorn
from fastapi import FastAPI
from pydantic import  BaseModel
from typing import List
from joblib import load

# definir modelo
class ModelFeatures(BaseModel):
    features: List[float]

app = FastAPI()

model = load('../model/model.pkl')

def get_prediction(features):

    if len(features) != len(model.coef_):
        return {'prediction': None}

    x = [features]
    y = model.predict(x)[0]
    return {'prediction': y}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
def post_predict(features: ModelFeatures):
    return get_prediction(features.features)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)