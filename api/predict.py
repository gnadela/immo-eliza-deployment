# predict.py

import pickle
import pandas as pd

# Load the trained model
with open("../model/trained_model.pkl", "rb") as f:
    model = pickle.load(f)

def preprocess_input(data):
    # Convert data to DataFrame
    input_data = pd.DataFrame([data])

    # Preprocess input data
    input_data["postal_zone"] = input_data["postal_zone"].astype(int)  # Convert postal_zone to int
    input_data = input_data.drop(columns=["zip_code"])  # Remove zip_code column

    return input_data

def predict(data):
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

    return predictions.tolist()


