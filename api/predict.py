import pickle
import pandas as pd

# Load the trained model
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

def preprocess_input(data):
    # Convert PropertyInput object to a dictionary
    data_dict = data.dict()

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame([data_dict])

    # Make zip_code a categorical value
    df['zip_code'] = df['zip_code'].astype('category')

    # Define categorical columns
    categorical_cols = ["property_type", "subproperty_type", "province", "locality", 
                        "equipped_kitchen", "state_building", "epc", "heating_type", "zip_code"]

    # Perform one-hot encoding for categorical variables
    df_encoded = pd.get_dummies(df, columns=categorical_cols)

    return df_encoded

def predict(data):
    # Preprocess input data
    input_data = preprocess_input(data)

    # Get all possible feature names based on preprocessing
    all_features = model.get_booster().feature_names

    # Ensure input data has all possible features, filling missing columns with zeros
    input_data_encoded = input_data.reindex(columns=all_features, fill_value=0)

    # Make predictions
    prediction = model.predict(input_data_encoded)

    return prediction
  