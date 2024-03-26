import requests

# Define the endpoint for retrieving feature order
feature_order_url = "http://127.0.0.1:8000/feature_order"

# Function to get feature order from the server
def get_feature_order():
    response = requests.get(feature_order_url)
    if response.status_code == 200:
        return response.json()["feature_order"]
    else:
        # Handle error
        print("Failed to retrieve feature order:", response.status_code)
        return None

# Get feature order from the server
features_order = get_feature_order()

if features_order:
    # Now you have the feature order, you can construct the input data dictionary accordingly
    input_data = {"total_area_sqm": 100,
    "property_type": "APARTMENT",
    "subproperty_type": "APARTMENT",
    "province": "Flemish Brabant",
    "locality": "Leuven",
    "zip_code": "3000",
    "latitude": 508335291,
    "longitude": 49429068,
    "construction_year": 2000,
    "surface_land_sqm": 150,
    "nbr_frontages": 2,
    "nbr_bedrooms": 2,
    "equipped_kitchen": "INSTALLED",
    "fl_furnished": 1,
    "fl_open_fire": 0,
    "fl_terrace": 1,
    "terrace_sqm": 20,
    "fl_garden": 1,
    "garden_sqm": 50,
    "fl_swimming_pool": 0,
    "fl_floodzone": 0,
    "state_building": "GOOD",
    "primary_energy_consumption_sqm": 150,
    "epc": "C",
    "heating_type": "GAS",
    "fl_double_glazing": 1,
    "postal_zone": "30"
    }
else:
    print("Feature order retrieval failed. Exiting.")
    exit()

# Send input data to the server for prediction
prediction_url = "http://127.0.0.1:8000/predict"
response = requests.post(prediction_url, json=input_data)

if response.status_code == 200:
    predictions = response.json()["predictions"]
    print("Predictions:", predictions)
else:
    print("Prediction request failed:", response.status_code)
