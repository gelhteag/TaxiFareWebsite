import streamlit as st


import requests

url = 'https://apitest-4c5uq47y5a-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


pickup_datetime = st.text_input('pickup_datetime', )
pickup_longitude = st.text_input('pickup_longitude', )
pickup_latitude = st.text_input('pickup_latitude', )
dropoff_longitude = st.text_input('dropoff_longitude', )
dropoff_latitude = st.text_input('dropoff_latitude', )
passenger_count = st.text_input('passenger_count', )
result = {
         'pickup_datetime': pickup_datetime,
         'pickup_longitude': pickup_longitude,
         'pickup_latitude': pickup_latitude,
         'dropoff_longitude': dropoff_longitude,
         'dropoff_latitude': dropoff_latitude,
         'passenger_count': passenger_count
     }


if st.button('Predict'):
    response = requests.get(url, params=result).json()
    st.json(response)
