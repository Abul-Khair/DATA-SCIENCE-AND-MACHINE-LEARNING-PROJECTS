import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model and scaler
model = joblib.load('dt_trained_model.joblib')  
scaler = joblib.load('scaler.joblib') 
# Ensure the model and scaler files are in the same directory or provide the correct path

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f4f4f4;
        padding: 20px;
        border-radius: 10px;
        max-width: 800px;
        margin: auto;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 8px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    h1, h3 {
        text-align: center;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .stSelectbox, .stSlider, .stNumberInput {
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title('Second Hand Car Price Prediction')
st.markdown("<h3>Enter the details below to predict the car price:</h3>", unsafe_allow_html=True)

# Sidebar with input features
with st.sidebar.form(key='car_form'):
    on_road_old = st.number_input('On Road Old Price (in rupees)', min_value=0, max_value=699859, value=300000)
    on_road_now = st.number_input('On Road Now Price (in rupees)', min_value=0, max_value=899797, value=350000)
    years = st.slider('Years', 0, 20, 5)
    km = st.number_input('Kilometers Driven', min_value=0, max_value=150000, value=50000)
    rating = st.slider('Rating (1 to 5)', 1.0, 5.0, 3.5, step=0.1)
    condition = st.slider('Condition (1 to 10)', 1, 10, 5)
    economy = st.number_input('Economy (km/l)', min_value=0.0, max_value=15.0, value=10.0, step=0.1)
    top_speed = st.number_input('Top Speed (km/h)', min_value=0, max_value=200, value=160, step=1)
    hp = st.number_input('Horsepower (hp)', min_value=0, max_value=120, value=80, step=1)
    torque = st.number_input('Torque (Nm)', min_value=0, max_value=150, value=100, step=1)
    submit_button = st.form_submit_button(label='Predict Price')

# Create input data DataFrame
input_data = pd.DataFrame({
    'on road old': [on_road_old],
    'on road now': [on_road_now],
    'years': [years],
    'km': [km],
    'rating': [rating],
    'condition': [condition],
    'economy': [economy],
    'top speed': [top_speed],
    'hp': [hp],
    'torque': [torque]
})

# Display input data for user confirmation
st.write("### Input Data", input_data)

# Make prediction when the button is clicked
if submit_button:
    try:
        # Scale the input data using the loaded scaler
        scaled_input_data = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(scaled_input_data)
        st.success(f'The predicted price of the car is rupees {prediction[0]:.2f}')
    except Exception as e:
        st.error(f"Error in prediction: {e}")
