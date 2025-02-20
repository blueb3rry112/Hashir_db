import streamlit as st
import pandas as pd 
import json 
import requests 

st.title("Hashir's wheather dashboard")
st.subheader("weather data")

lattitude = st.sidebar.number_input("enter lattitude",value=0.0)
longitude = st.sidebar.number_input("enter longitude",value=0.0) 

api_url = f'https://api.open-meteo.com/v1/forecast?latitude={lattitude}&longitude={longitude}&current=temperature_2m,is_day,showers,wind_direction_10m&hourly=temperature_2m,rain,snowfall'

resp = requests.get(api_url) 
value = json.loads(resp.text)

selectbox_option = st.sidebar.selectbox(
    'select the data to visualize' ,
    ('Temperature' , 'rain' , 'snowfall')
)



temp = value["current"]["temperature_2m"]
day = value["current"]["is_day"]
shower = value["current"]["showers"]
wind_direction = value["current"]["wind_direction_10m"]

def day_or_night():
    return "Day" if day == 1 else "night"


col1, col2, col3, col4, = st.columns(4)
with col1:
    st.metric('Temperature ',temp)

with col2:
    st.metric('Day or Night',day_or_night())

with col3:
    st.metric("Shower",shower)

with col4:
    st.metric("Wind direction",wind_direction)


st.image ("https://cdn.pixabay.com/photo/2024/02/26/20/48/landscape-8598886_1280.jpg")

st.video ("https://youtu.be/yrOYxLt9SCI?si=vcVyg3YQ0LDOII3G")



hourly_twmp_df = pd.DataFrame(value["hourly"]["temperature_2m"],
                                 value["hourly"]["time"] )
hourly_rain_df = pd.DataFrame(value["hourly"]["rain"],
                                 value["hourly"]["time"] )
hourly_snow_df = pd.DataFrame(value["hourly"]["snowfall"],
                                 value["hourly"]["time"] )



if selectbox_option == 'Temperature':
    st.line_chart(hourly_twmp_df)
elif selectbox_option == 'rain':
    st.line_chart(hourly_rain_df)
else:
    st.line_chart(hourly_snow_df)

