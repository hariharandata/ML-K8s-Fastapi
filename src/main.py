from pathlib import Path

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load the model
model_path = Path(__file__).parent / "iris_model.pkl"
model = joblib.load(model_path)

# Define the input data model
class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define the prediction model
@app.post("/predict")
def predict(input_data: InputData):
    # Convert the input data to a numpy array
    input_array = np.array([input_data.sepal_length, input_data.sepal_width, input_data.petal_length, input_data.petal_width])
    # Make the prediction
    prediction = model.predict(input_array.reshape(1, -1))
    # Return the prediction
    return {"prediction": int(prediction[0])}
