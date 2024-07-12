import streamlit as st
import requests
import datetime
import pandas as pd

# Title of the web application
st.title('TaxiFareModel front')

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

# User input for ride parameters
st.header("Select the parameters of the ride")

date = st.date_input("Date of pickup", datetime.date.today())
time = st.time_input("Time of pickup", datetime.datetime.now().time())
pickup_longitude = st.number_input("Pickup Longitude", value=0.0)
pickup_latitude = st.number_input("Pickup Latitude", value=0.0)
dropoff_longitude = st.number_input("Dropoff Longitude", value=0.0)
dropoff_latitude = st.number_input("Dropoff Latitude", value=0.0)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

# Create datetime string from date and time inputs
pickup_datetime = f"{date} {time}"

# API URL
url = 'https://taxifare.lewagon.ai/predict'

# Display a message indicating which API is being used
st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# If the 'Predict' button is pressed
if st.button('Predict'):

    # Build the dictionary containing the parameters for the API
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Call the API using the `requests` package
    response = requests.get(url, params=params)
    prediction = response.json()

    # Display the prediction
    st.header('Prediction')
    st.write(f"The predicted fare is: ${prediction['fare_amount']:.2f}")

    # Display the map with pickup and dropoff points
    st.subheader('Map of Ride')
    ride_map = pd.DataFrame({
        'lat': [pickup_latitude, dropoff_latitude],
        'lon': [pickup_longitude, dropoff_longitude]
    })

    st.map(ride_map)
