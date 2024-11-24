import streamlit as st
import requests

st.title("Weather Information")
city = st.text_input("Enter a city name")

if city:
    api_key = "c629cdf4f325588605dd605ffe9eb865"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.write(f"**Temperature:** {data['main']['temp']}°C")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Weather:** {data['weather'][0]['description'].capitalize()}")
    else:
        st.error("City not found or API error.")
