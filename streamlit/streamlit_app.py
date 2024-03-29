import streamlit as st
import requests
from pydantic import BaseModel

# Define FastAPI server URL
API_URL = "http://localhost:8000/predict"

# Define the input fields
class PropertyInput(BaseModel):
    total_area_sqm: float = 0.0
    property_type: str = ""
    subproperty_type: str = ""
    province: str = ""
    locality: str = ""
    zip_code: str = ""
    construction_year: float = 0.0
    surface_land_sqm: float = 0.0
    nbr_frontages: float = 0.0
    nbr_bedrooms: float = 0.0
    equipped_kitchen: str = ""
    fl_furnished: int = 0
    fl_open_fire: int = 0
    fl_terrace: int = 0
    terrace_sqm: float = 0.0
    fl_garden: int = 0
    garden_sqm: float = 0.0
    fl_swimming_pool: int = 0
    fl_floodzone: int = 0
    state_building: str = ""
    primary_energy_consumption_sqm: float = 0.0
    epc: str = ""
    heating_type: str = ""
    fl_double_glazing: int = 0
    
def predict_price(data: PropertyInput):
    response = requests.post(API_URL, json=data.dict())
    if response.status_code == 200:
        # Extract the predicted price from the HTML content
        predicted_price_raw = response.text.split('€')[1].strip()
        # Clean up the predicted price
        predicted_price = predicted_price_raw.split('<')[0].strip()
        # Format the predicted price as 'euro 111,111.00'
        formatted_prediction = f"€ {float(predicted_price):,.2f}"
        return formatted_prediction
 #       return predicted_price
    else:
        return None

def main():
    st.title("Property Price Predictor")

    st.sidebar.title("Input Fields")
    pre_filled_data = {
        "total_area_sqm": st.sidebar.number_input('Total Area (sqm)', value=125.0),
        "property_type": st.sidebar.selectbox('Property Type', ['HOUSE', 'APARTMENT']),
        "subproperty_type": st.sidebar.selectbox('Subproperty Type', ['APARTMENT', 'HOUSE', 'DUPLEX', 'VILLA', 'EXCEPTIONAL_PROPERTY', 'FLAT_STUDIO', 'GROUND_FLOOR', 'PENTHOUSE', 'FARMHOUSE', 'APARTMENT_BLOCK', 'COUNTRY_COTTAGE', 'TOWN_HOUSE', 'SERVICE_FLAT', 'MANSION', 'MIXED_USE_BUILDING', 'MANOR_HOUSE', 'LOFT', 'BUNGALOW', 'KOT', 'CASTLE', 'CHALET', 'OTHER_PROPERTY', 'TRIPLEX']),
        "province": st.sidebar.selectbox('Province', ['Antwerp', 'East Flanders', 'Brussels', 'Walloon Brabant', 'Flemish Brabant', 'Liege', 'West Flanders', 'Hainaut', 'Luxembourg', 'Limburg', 'Namur']),
        "locality": st.sidebar.selectbox('Locality', ['Aalst', 'Antwerp', 'Arlon', 'Ath', 'Bastogne', 'Brugge', 'Brussels', 'Charleroi', 'Dendermonde', 'Diksmuide', 'Dinant', 'Eeklo', 'Gent', 'Halle-Vilvoorde', 'Hasselt', 'Huy', 'Ieper', 'Kortrijk', 'Leuven', 'Liège', 'Maaseik', 'Marche-en-Famenne', 'Mechelen', 'Mons', 'Mouscron', 'Namur', 'NeufchÃ¢teau', 'Nivelles', 'Oostend', 'Oudenaarde', 'Philippeville', 'Roeselare', 'Sint-Niklaas', 'Soignies', 'Thuin', 'Tielt', 'Tongeren', 'Tournai', 'Turnhout', 'Verviers', 'Veurne', 'Virton', 'Waremme']),
        "zip_code": st.sidebar.text_input('Zip Code', value="1000"),
        "construction_year": st.sidebar.number_input('Construction Year', value=1993),
        "surface_land_sqm": st.sidebar.number_input('Surface Land (sqm)', value=360.0),
        "nbr_frontages": st.sidebar.number_input('Number of Frontages', value=3),
        "nbr_bedrooms": st.sidebar.number_input('Number of Bedrooms', value=1),
        "equipped_kitchen": st.sidebar.selectbox('Equipped Kitchen', ['HYPER_EQUIPPED', 'INSTALLED', 'NOT_INSTALLED', 'SEMI_EQUIPPED', 'USA_HYPER_EQUIPPED', 'USA_INSTALLED', 'USA_SEMI_EQUIPPED', 'USA_UNINSTALLED']),
        "fl_furnished": st.sidebar.checkbox('Furnished'),
        "fl_open_fire": st.sidebar.checkbox('Open Fire'),
        "fl_terrace": st.sidebar.checkbox('Terrace'),
        "terrace_sqm": st.sidebar.number_input('Terrace (sqm)', value=1.0),
        "fl_garden": st.sidebar.checkbox('Garden'),
        "garden_sqm": st.sidebar.number_input('Garden (sqm)', value=0.0),
        "fl_swimming_pool": st.sidebar.checkbox('Swimming Pool'),
        "fl_floodzone": st.sidebar.checkbox('Flood Zone'),
        "state_building": st.sidebar.selectbox('State Building', ['AS_NEW', 'GOOD', 'JUST_RENOVATED', 'TO_BE_DONE_UP', 'TO_RENOVATE', 'TO_RESTORE']),
        "primary_energy_consumption_sqm": st.sidebar.number_input('Primary Energy Consumption (sqm)', value=245.0),
        "epc": st.sidebar.selectbox('Energy Performance Certificate', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        "heating_type": st.sidebar.selectbox('Heating Type', ['CARBON', 'ELECTRIC', 'FUELOIL', 'GAS', 'MISSING', 'PELLET', 'SOLAR', 'WOOD']),
        "fl_double_glazing": st.sidebar.checkbox('Double Glazing')
    }

    if st.button("Predict Price"):
        input_data = PropertyInput(
            total_area_sqm=pre_filled_data['total_area_sqm'],
            property_type=pre_filled_data['property_type'],
            subproperty_type=pre_filled_data['subproperty_type'],
            province=pre_filled_data['province'],
            locality=pre_filled_data['locality'],
            zip_code=pre_filled_data['zip_code'],
            construction_year=pre_filled_data['construction_year'],
            surface_land_sqm=pre_filled_data["surface_land_sqm"],
            nbr_frontages=pre_filled_data["nbr_frontages"],
            nbr_bedrooms=pre_filled_data["nbr_bedrooms"],
            equipped_kitchen=pre_filled_data["equipped_kitchen"],
            fl_furnished=pre_filled_data["fl_furnished"],
            fl_open_fire=pre_filled_data["fl_open_fire"],
            fl_terrace=pre_filled_data["fl_terrace"],
            terrace_sqm=pre_filled_data["terrace_sqm"],
            fl_garden=pre_filled_data["fl_garden"],
            garden_sqm=pre_filled_data["garden_sqm"],
            fl_swimming_pool=pre_filled_data["fl_swimming_pool"],
            fl_floodzone=pre_filled_data["fl_floodzone"],
            state_building=pre_filled_data["state_building"],
            primary_energy_consumption_sqm=pre_filled_data["primary_energy_consumption_sqm"],
            epc=pre_filled_data["epc"],
            heating_type=pre_filled_data["heating_type"],
            fl_double_glazing=pre_filled_data["fl_double_glazing"]
        )
        prediction = predict_price(input_data)
        if prediction is not None:
            st.success(f"Predicted Price: {prediction}")
        else:
            st.error("Failed to predict price. Please try again.")
        

if __name__ == "__main__":
    main()
