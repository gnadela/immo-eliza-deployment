from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI()

class PropertyInput(BaseModel):
    total_area_sqm: float
    property_type: str
    subproperty_type: str
    province: str
    locality: str
    zip_code: str
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

@app.get('/')
def root():
    return 'Immo Eliza Prediction Site'

@app.post("/predict/")
async def predict_price(data: PropertyInput):
    prediction = predict(data)

    # Convert NumPy array to list for JSON serialization
    prediction = prediction.tolist()

    return prediction