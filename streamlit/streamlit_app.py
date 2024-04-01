import streamlit as st
import requests

# Define URL of the FastAPI server
FASTAPI_URL = "http://localhost:8000/predict"

# Initialize pre-filled data dictionary
pre_filled_data = {
    "total_area_sqm": st.sidebar.number_input('Total Area (sqm)', value=125.0),
    "property_type": st.sidebar.selectbox('Property Type', ['HOUSE', 'APARTMENT']),
    "subproperty_type": st.sidebar.selectbox('Subproperty Type', ['APARTMENT', 'HOUSE', 'DUPLEX', 'VILLA', 'EXCEPTIONAL_PROPERTY', 'FLAT_STUDIO', 'GROUND_FLOOR', 'PENTHOUSE', 'FARMHOUSE', 'APARTMENT_BLOCK', 'COUNTRY_COTTAGE', 'TOWN_HOUSE', 'SERVICE_FLAT', 'MANSION', 'MIXED_USE_BUILDING', 'MANOR_HOUSE', 'LOFT', 'BUNGALOW', 'KOT', 'CASTLE', 'CHALET', 'OTHER_PROPERTY', 'TRIPLEX']),
    "province": st.sidebar.selectbox('Province', ['Antwerp', 'East Flanders', 'Brussels', 'Walloon Brabant', 'Flemish Brabant', 'Liege', 'West Flanders', 'Hainaut', 'Luxembourg', 'Limburg', 'Namur']),
    "locality": st.sidebar.selectbox('Locality', ['Aalst', 'Antwerp', 'Arlon', 'Ath', 'Bastogne', 'Brugge', 'Brussels', 'Charleroi', 'Dendermonde', 'Diksmuide', 'Dinant', 'Eeklo', 'Gent', 'Halle-Vilvoorde', 'Hasselt', 'Huy', 'Ieper', 'Kortrijk', 'Leuven', 'LiÃ¨ge', 'Maaseik', 'Marche-en-Famenne', 'Mechelen', 'Mons', 'Mouscron', 'Namur', 'NeufchÃ¢teau', 'Nivelles', 'Oostend', 'Oudenaarde', 'Philippeville', 'Roeselare', 'Sint-Niklaas', 'Soignies', 'Thuin', 'Tielt', 'Tongeren', 'Tournai', 'Turnhout', 'Verviers', 'Veurne', 'Virton', 'Waremme']),
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

# Send pre-filled data to FastAPI server for prediction
response = requests.post(FASTAPI_URL, json=pre_filled_data)

# Get the predicted price from the response
predicted_price = response.json()[0]

predicted_price_formatted = "€ {:,.2f} ".format(predicted_price)
st.write("Predicted Price:", predicted_price_formatted)
  