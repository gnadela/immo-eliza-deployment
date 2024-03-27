# client.py

import requests

input_data = {
 "zip_code": "3001",
"latitude": 508335290,
"longitude": 49429068,
"construction_year": 2000,
"total_area_sqm": 1000,
"surface_land_sqm": 150,
"nbr_frontages": 4,
"nbr_bedrooms": 2,
"fl_furnished": 1,
"fl_open_fire": 0,
"fl_terrace": 1,
"terrace_sqm": 20,
"fl_garden": 1,
"garden_sqm": 50,
"fl_swimming_pool": 0,
"fl_floodzone": 0, 
"primary_energy_consumption_sqm": 150,
"fl_double_glazing": 1,
"property_type": "HOUSE",
"subproperty_type": "VILLA",
"province": "Flemish Brabant",
"locality": "Leuven",
"equipped_kitchen": "INSTALLED",
"state_building": "GOOD",
"epc": "C",
"heating_type": "GAS",
"postal_zone": "30"
}

# Send the POST request to the server
prediction_url = "http://127.0.0.1:8000/predict"
response = requests.post(prediction_url, json=input_data)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    # Display the predictions
    print("Prediction:", response_data["predictions"])
else:
    # Display an error message if the request fails
    print("Prediction request failed:", response.status_code)

