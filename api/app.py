from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from predict import predict

app = FastAPI()
templates = Jinja2Templates(directory="templates")

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

# Define pre-filled data outside of any function
pre_filled_data = PropertyInput(
    total_area_sqm=100,
    property_type="APARTMENT",
    subproperty_type="APARTMENT",
    province="Flemish Brabant",
    locality="Leuven",
    zip_code="3000",
    construction_year=2000,
    surface_land_sqm=150,
    nbr_frontages=2,
    nbr_bedrooms=2,
    equipped_kitchen="INSTALLED",
    fl_furnished=1,
    fl_open_fire=0,
    fl_terrace=1,
    terrace_sqm=20,
    fl_garden=1,
    garden_sqm=50,
    fl_swimming_pool=0,
    fl_floodzone=0,
    state_building="GOOD",
    primary_energy_consumption_sqm=150,
    epc="C",
    heating_type="GAS",
    fl_double_glazing=1
)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    print("pre_filled_data:", pre_filled_data)  # Add this line for debugging
    return templates.TemplateResponse("index.html", {"request": request, "data": pre_filled_data})

@app.post("/predict/", response_class=HTMLResponse)
async def predict_price(request: Request, data: PropertyInput):
    try:
        # Call the predict function from predict.py
        prediction = predict(data)
        return templates.TemplateResponse("prediction_result.html", {"request": request, "prediction": prediction})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)