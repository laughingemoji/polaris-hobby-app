import reverse_geocode
import streamlit as st
import pandas as pd
import numpy as np
import requests
from requests.structures import CaseInsensitiveDict
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="http")

url = "https://nearby-places.p.rapidapi.com/v2/nearby"

querystring = {"lat": "26", "lng": "-80", "radius": "1000"}

headers = {
    "X-RapidAPI-Host": "nearby-places.p.rapidapi.com",
    "X-RapidAPI-Key": "d9fb350effmsh4494ebe218be745p172f81jsna3cdf3b83675"
}

response = requests.request("GET", url, headers=headers, params=querystring)

st.set_page_config(
    page_title="Polaris",
    page_icon="📍",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a Bug': 'https://github.com/streamlit/streamlit/issues/new/choose',
        'About': '# Welcome to Polaris!\n This website was made to help people find different interests and '
                 'help explore passions. It is fully curated by you! Add your personal specifications and Polaris will'
                 'take care of the rest!'
    }
)

st.title = "Polaris"
st.header("Polaris: The Hobby App")
st.write("👈Please fill out the interests form on the top left menu to get started.")

coord1 = None
coord2 = None
location = None

# Hobbies/Interests Questionnaire
with st.sidebar:
    agree = st.checkbox('Click here to start!')
    if agree:
        age = st.number_input('Enter Your Age', min_value=1.0,
                              max_value=100.0,
                              step=1.0,
                              )
        # Location section
        st.write("Enter a location: ")
        col1, col2 = st.columns(2)
        with col1:
            coord1 = st.text_input("Latitude")
        with col2:
            coord2 = st.text_input("Longitude")
        if coord1 and coord2:
            coords_list = [coord1, coord2]
            location = geolocator.reverse(coords_list)
            # coordinates = (coord1, coord2)
            # reverse_geocode.search(coordinates)

        hobby = st.radio(
            "Do you consider your hobbies extroverted or introverted?",
            ('Extroverted', 'Introverted'))
        if hobby == 'Extroverted':
            exvalues = st.slider(
                'How extroverted are you on a scale of 1-10?',
                0.0, 10.0, 5.0)
            invalues = 0
            st.write('You are:', exvalues, hobby)

        if hobby == "Introverted":
            invalues = st.slider(
                'How introverted are you on a scale of 1-10?',
                0.0, 10.0, 5.0)
            exvalues = 0
            st.write('You are:', invalues, hobby)

        if exvalues == 0:
            exvalues = invalues - 10
            chart_data = pd.DataFrame({
                "Introverted": [invalues],
                "Extroverted": [exvalues]}
            )

        if invalues == 0:
            invalues = exvalues - 10
            chart_data = pd.DataFrame({
                "Introverted": [invalues],
                "Extroverted": [exvalues]}
            )

        st.bar_chart(chart_data)

<<<<<<< HEAD
=======
        st.write("Certain hobbies can be described as being introverted or extroverted activities. Such as:")
        df = pd.DataFrame({
            "Hobby": ['Sports', 'Gaming', 'Art', 'Music', 'Reading', 'Partying'],
            "Type": ['Extroverted', 'Introverted', 'Introverted', 'Introverted', 'Introverted', 'Extroverted']
        })
        st.dataframe(df)
        
>>>>>>> 012f8d958e169c347b59921ea1327c372289293e
        options = st.multiselect(
            'What do you like?',
            (['Sports', 'Gaming', 'Art', 'Music', 'Reading', 'Partying']))
        if options:
            st.write('You like:')
            for x in options:
                st.text(x)

col3, col4 = st.columns(2)
with col3:
    # Displaying the Map
    st.subheader("🗺️Map")
    if coord1 and coord2:
        df = pd.DataFrame({
            'lat': [float(coord1)],
            'lon': [float(coord2)], })
        st.dataframe(df)
        st.map(df)
        st.success("Map Successfully formed")
    else:
        st.error("Empty or invalid coordinates!")

    result = st.button("When you are finished click")
    if result:
        st.write("Thank you ::thumbsup:")
with col4:
    # Displaying Locations/Events/Addresses
    st.subheader("📍Locations")
    st.write(location)
    st.write(response.text)
