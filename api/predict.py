import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# Load the trained model
with open("../model/trained_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class PropertyInput(BaseModel):
    total_area_sqm: float
    property_type: str
    subproperty_type: str
    province: str
    locality: str
    zip_code: str
    latitude: float
    longitude: float
    construction_year: float
    surface_land_sqm: float
    nbr_frontages: float
    nbr_bedrooms: float
    equipped_kitchen: str
    fl_furnished: int
    fl_open_fire: int
    fl_terrace: int
    terrace_sqm: float
    fl_garden: int
    garden_sqm: float
    fl_swimming_pool: int
    fl_floodzone: int
    state_building: str
    primary_energy_consumption_sqm: float
    epc: str
    heating_type: str
    fl_double_glazing: int
    postal_zone: str

def preprocess_input(data):
    # Convert data to DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Preprocess input data
    input_data["postal_zone"] = input_data["postal_zone"].astype(int) # Convert postal_zone to int
    input_data = input_data.drop(columns=["zip_code"]) # Remove zip_code column
    # Add missing "postal_zone_3000" column filled with zeros
    input_data["postal_zone_3000"] = 0

    return input_data

@app.post("/predict/")
async def predict(data: PropertyInput):
    # Preprocess input data
    input_data = preprocess_input(data)

    # Perform one-hot encoding for categorical variables
    categorical_cols = ["property_type", "subproperty_type", "province", "locality", "equipped_kitchen", "state_building", "epc", "heating_type", "postal_zone"]
    input_data_encoded = pd.get_dummies(input_data, columns=categorical_cols)

    # Get all possible feature names based on preprocessing
    all_features = model.get_booster().feature_names

    # Ensure input data has all possible features, filling missing columns with zeros
    input_data_encoded = input_data_encoded.reindex(columns=all_features, fill_value=0)

    # Make predictions
    predictions = model.predict(input_data_encoded)

    result = {"predictions": predictions.tolist()}

    return result

@app.get("/feature_order")
async def get_feature_order():
    # Get feature names from the trained XGBoost model
    feature_order = model.get_booster().feature_names

    return {"feature_order": feature_order}
