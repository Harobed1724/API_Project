from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import logging
 
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sepsis-prediction")
 
app = FastAPI()
 
# Define the model file path
model_path = r"C:/Users/debor/Downloads/Azubi Africa/Project/API_Project/API_Project/Models/best_model_rf.pkl"
 
# Verify file path and load the model
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")
 
try:
    sepsis_model = joblib.load(model_path)
    logger.info("Model loaded successfully.")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")
 
# Define the data model for incoming requests
class PatientData(BaseModel):
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: int
    Insurance: int
 
# Root route for basic API status
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Sepsis Prediction API! Use /predict_sepsis to make predictions."}
 
# Endpoint for sepsis prediction
@app.post("/predict_sepsis")
async def predict_sepsis(data: PatientData):
    try:
        # Prepare input data for the model
        input_data = [[
            data.PRG, data.PL, data.PR, data.SK, data.TS, data.M11, data.BD2, data.Age, data.Insurance
        ]]
 
        # Perform prediction
        prediction = sepsis_model.predict(input_data)
 
        # Return prediction result
        return JSONResponse(content={"prediction": int(prediction[0])}, status_code=200)
 
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
 
# Endpoint to upload a CSV file and make predictions
@app.post("/predict_sepsis_csv")
async def predict_sepsis_csv(file: UploadFile = File(...)):
    try:
        # Read the uploaded file into a DataFrame
        df = pd.read_csv(file.file)
 
        # Check for required columns
        required_columns = ["PRG", "PL", "PR", "SK", "TS", "M11", "BD2", "Age", "Insurance"]
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"Missing required columns. Expected columns: {required_columns}")
 
        # Perform predictions
        predictions = sepsis_model.predict(df[required_columns])
        df["Prediction"] = predictions
 
        # Convert predictions to JSON and return
        return JSONResponse(content=df.to_dict(orient="records"), status_code=200)
 
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
 
# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("myapi:app", port=8000, reload=True)
