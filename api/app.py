from fastapi import FastAPI, HTTPException
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

@app.get("/")
async def root():
    return {"message": "I am alive"}

@app.post("/predict/")
async def predict_price(data: PropertyInput):
    try:
        # Call the predict function from predict.py
        prediction = predict(data.dict())
        return {"predictions": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#@app.get("/feature_order")
#async def get_features():
#    try:
        # Call the get_feature_order function from predict.py
#        features = get_feature_order()
#        return {"feature_order": features}
#    except Exception as e:
#        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)