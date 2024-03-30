import pickle
import pandas as pd

# Load the trained model
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

def preprocess_input(data):
    data_dict = data.dict()
    df = pd.DataFrame([data_dict])

    # convert zip code into categorical data
    df = df['zip_code'].astype('category')

    categorical_cols = ["property_type", "subproperty_type", "province", "locality", 
                        "equipped_kitchen", "state_building", "epc", "heating_type", "zip_code"]

    # one-hot-encoding
    df_encoded = pd.get_dummies(df, columns=categorical_cols)

    all_features = model.get_booster().feature_names

    # fill blanks
    df_encoded = df_encoded.reindex(columns=all_features, fill_value=0)

    return df_encoded

def predict(data):
    input_data = preprocess_input(data)
    prediction = model.predict(input_data)

    return prediction
