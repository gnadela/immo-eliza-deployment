import pickle
import pandas as pd
import os
import numpy as np
import xgboost

model_file_path = "C:\\Users\\gnade\\OneDrive\\Desktop\\PythonProjects\\immo-eliza-deployment\\streamlit\\trained_model.pkl"

print("File exists:", os.path.exists(model_file_path))
print("Is a file:", os.path.isfile(model_file_path))

# Load the model if the file exists
if os.path.exists(model_file_path) and os.path.isfile(model_file_path):
    with open(model_file_path, "rb") as f:
        # Read the model
        # Your model loading code goes here
        # Load the trained model
        model = pickle.load(f)
else:
    print("Model file does not exist or is not a file.")

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
    try:    
        # Preprocess input data
        input_data = preprocess_input(data)
        print("Input data after preprocessing:")
        print(input_data)

        # Get all possible feature names based on preprocessing
        all_features = model.get_booster().feature_names
        print("All features:", all_features)

        # Ensure input data has all possible features, filling missing columns with zeros
        input_data_encoded = input_data.reindex(columns=all_features, fill_value=0)
        print("Input data encoded with all features:")
        print(input_data_encoded)

        # Make predictions
        prediction = model.predict(input_data_encoded)
        print("Raw prediction:", prediction)

        if prediction is None or len(prediction) == 0:
            return "No prediction available"

        # Ensure prediction is a scalar value
        prediction_scalar = prediction.item() if isinstance(prediction, np.ndarray) and prediction.size == 1 else prediction
        print("Final prediction:", prediction_scalar)

        return prediction_scalar
    
    except Exception as e:
        # Print the exception for debugging
        print("An error occurred during prediction:", e)
        return None
