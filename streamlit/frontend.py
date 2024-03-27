import streamlit as st
import requests

# Define the FastAPI server URL
FASTAPI_URL = 'http://localhost:8000'

# Define the endpoint for making predictions
PREDICTION_ENDPOINT = '/predict/'

# Main Streamlit app
def main():
    st.title('ImmoEliza Prediction App')

    # Input fields
    st.sidebar.header('Input Parameters')
    total_area_sqm = st.sidebar.number_input('Total Area (sqm)', value=100.0)
    latitude = st.sidebar.number_input('Latitude', value=50.0)
    # Add other input fields as needed...

    # Prediction button
    if st.sidebar.button('Predict'):
        # Prepare input data
        input_data = {
            "total_area_sqm": total_area_sqm,
            "latitude": latitude,
            # Add other input fields here...
        }

        # Make request to FastAPI backend for prediction
        response = requests.post(f'{FASTAPI_URL}{PREDICTION_ENDPOINT}', json=input_data)

        # Display prediction result
        if response.status_code == 200:
            predictions = response.json()["predictions"]
            st.success(f'Predicted Price: {predictions[0]}')
        else:
            st.error('Failed to get prediction from the server.')

if __name__ == '__main__':
    main()
