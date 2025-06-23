from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# Load model
model_path = os.getenv("MODEL_PATH", "/data/model.pkl")
model = joblib.load(model_path)

# Define input schema for Iris (4 features)
class PredictionInput(BaseModel):
    features: list[float]  # Exactly 4 features for Iris

@app.post("/predict")
async def predict(input_data: PredictionInput):
    if len(input_data.features) != 4:
        raise ValueError("Input must contain exactly 4 features")
    features = pd.DataFrame([input_data.features])
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}