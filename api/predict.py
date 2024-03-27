import pickle
import pandas as pd

# Load the trained model
with open("../model/trained_model.pkl", "rb") as f:
    model = pickle.load(f)

def preprocess_input(data):
    # Convert PropertyInput object to a dictionary
    data_dict = data.dict()

    # Convert the dictionary to a DataFrame
    data_df = pd.DataFrame([data_dict])

    return data_df

def predict(data):
    try:
        # Preprocess input data
        input_data = preprocess_input(data)
        input_data['zip_code'] = input_data['zip_code'].astype('category')

        # Define categorical columns
        categorical_cols = ["property_type", "subproperty_type", "province", "locality", 
                            "equipped_kitchen", "state_building", "epc", "heating_type", "zip_code"]

        # Perform one-hot encoding for categorical variables
        input_data_encoded = pd.get_dummies(input_data, columns=categorical_cols)

        # Get all possible feature names based on preprocessing
        all_features = model.get_booster().feature_names

        # Ensure input data has all possible features, filling missing columns with zeros
        input_data_encoded = input_data_encoded.reindex(columns=all_features, fill_value=0)

        # Make predictions
        predictions = model.predict(input_data_encoded)

        return predictions.tolist()
    except Exception as e:
        raise ValueError(str(e))

