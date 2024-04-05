import streamlit as st
import numpy as np
from pydantic import BaseModel
from spredict import predict 

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

def get_prediction(data):
    prediction = predict(data)
    return prediction

def format_currency(amount):
    if isinstance(amount, np.ndarray):
        amount = amount.item()  # Extract numeric value from NumPy array
    return f"€ {amount:,.2f}"

def main():
    st.title('Immo Eliza Property Prediction Site')

    # Pre-fill input fields with pre_filled_data
    pre_filled_data = {
        "property_type": st.sidebar.selectbox('Property Type', ['HOUSE', 'APARTMENT']),
        "subproperty_type": st.sidebar.selectbox('Subproperty Type', ['APARTMENT', 'HOUSE', 'DUPLEX', 'VILLA', 'EXCEPTIONAL_PROPERTY', 'FLAT_STUDIO', 'GROUND_FLOOR', 'PENTHOUSE', 'FARMHOUSE', 'APARTMENT_BLOCK', 'COUNTRY_COTTAGE', 'TOWN_HOUSE', 'SERVICE_FLAT', 'MANSION', 'MIXED_USE_BUILDING', 'MANOR_HOUSE', 'LOFT', 'BUNGALOW', 'KOT', 'CASTLE', 'CHALET', 'OTHER_PROPERTY', 'TRIPLEX']),
        "nbr_bedrooms": st.sidebar.number_input('Number of Bedrooms', value=1),
        "nbr_frontages": st.sidebar.number_input('Number of Frontages', value=3),
        "province": st.sidebar.selectbox('Province', ['Antwerp', 'East Flanders', 'Brussels', 'Walloon Brabant', 'Flemish Brabant', 'Liege', 'West Flanders', 'Hainaut', 'Luxembourg', 'Limburg', 'Namur']),
        "locality": st.sidebar.selectbox('Locality', ['Aalst', 'Antwerp', 'Arlon', 'Ath', 'Bastogne', 'Brugge', 'Brussels', 'Charleroi', 'Dendermonde', 'Diksmuide', 'Dinant', 'Eeklo', 'Gent', 'Halle-Vilvoorde', 'Hasselt', 'Huy', 'Ieper', 'Kortrijk', 'Leuven', 'Liège', 'Maaseik', 'Marche-en-Famenne', 'Mechelen', 'Mons', 'Mouscron', 'Namur', 'Neufchâteau', 'Nivelles', 'Oostend', 'Oudenaarde', 'Philippeville', 'Roeselare', 'Sint-Niklaas', 'Soignies', 'Thuin', 'Tielt', 'Tongeren', 'Tournai', 'Turnhout', 'Verviers', 'Veurne', 'Virton', 'Waremme']),
        "zip_code": st.sidebar.text_input('Zip Code', value="1000"),
        "fl_floodzone": st.sidebar.checkbox('Flood Zone'),
        "total_area_sqm": st.sidebar.number_input('Living Area (sqm)', value=125.0),
        "surface_land_sqm": st.sidebar.number_input('Surface Land (sqm)', value=360.0),
        "fl_garden": st.sidebar.checkbox('Garden'),
        "garden_sqm": st.sidebar.number_input('Garden (sqm)', value=0.0),
        "fl_swimming_pool": st.sidebar.checkbox('Swimming Pool'),
        "fl_terrace": st.sidebar.checkbox('Terrace'),
        "terrace_sqm": st.sidebar.number_input('Terrace (sqm)', value=1.0),
        "construction_year": st.sidebar.number_input('Construction Year', value=1993),
        "state_building": st.sidebar.selectbox('State Building', ['AS_NEW', 'GOOD', 'JUST_RENOVATED', 'TO_BE_DONE_UP', 'TO_RENOVATE', 'TO_RESTORE']),
        "equipped_kitchen": st.sidebar.selectbox('Equipped Kitchen', ['HYPER_EQUIPPED', 'INSTALLED', 'NOT_INSTALLED', 'SEMI_EQUIPPED', 'USA_HYPER_EQUIPPED', 'USA_INSTALLED', 'USA_SEMI_EQUIPPED', 'USA_UNINSTALLED']),
        "fl_furnished": st.sidebar.checkbox('Furnished'),
        "fl_open_fire": st.sidebar.checkbox('Open Fire'),
        "heating_type": st.sidebar.selectbox('Heating Type', ['CARBON', 'ELECTRIC', 'FUELOIL', 'GAS', 'MISSING', 'PELLET', 'SOLAR', 'WOOD']),
        "fl_double_glazing": st.sidebar.checkbox('Double Glazing'),
        "epc": st.sidebar.selectbox('Energy Performance Certificate', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        "primary_energy_consumption_sqm": st.sidebar.number_input('Primary Energy Consumption (sqm)', value=245.0)
    }

    # Convert pre-filled data to PropertyInput object
    data = PropertyInput(**pre_filled_data)

    # Create a button to trigger the prediction
    if st.button('Predict'):
        try:
            # Call the function to get the prediction
            prediction = get_prediction(data)
            formatted_prediction = format_currency(prediction)
            st.success(f'Price Prediction: {formatted_prediction}')
        except ConnectionError:
            st.error('Failed to connect to prediction service.')

if __name__ == '__main__':
    main()
