import time
import googlemaps
import streamlit as st
import pandas as pd
import numpy as np

API_KEY = 'AIzaSyCCDa3eBvAPo5LEwML9-e7calmLuSSyrwQ'
map_client = googlemaps.Client(API_KEY)


def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0


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
business_list = []
search_string = ""
distance = miles_to_meters(10)

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

        st.write("Certain hobbies can be described as being introverted or extroverted activities. Such as:")
        df = pd.DataFrame({
            "Hobby": ['Sports', 'Gaming', 'Art', 'Music', 'Reading', 'Partying'],
            "Type": ['Extroverted', 'Introverted', 'Introverted', 'Introverted', 'Introverted', 'Extroverted']
        })
        st.dataframe(df)

        options = st.multiselect(
            'What would you like to search for?',
            (['Sports', 'Gaming', 'Art', 'Music', 'Reading', 'Partying']))
        if options:
            st.write('You like:')
            # This will search up the locations based on whatever hobby they chose
            search_string = options[0]
            # Or, we pre-select a few categories based off what they pick
            if search_string == "Sports":
                search_string = "kids arcade"
            elif search_string == "Gaming":
                search_string = "VR"
            elif search_string == "Art":
                search_string = "gallery"
            elif search_string == "Music":
                search_string = "concert"
            elif search_string == "Reading":
                search_string = "book"
            elif search_string == "Partying":
                search_string = "club"
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
    if coord1 and coord2:
        response = map_client.places_nearby(
            location=(coord1, coord2),
            keyword=search_string,
            radius=distance
        )
        business_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')
        while next_page_token:
            time.sleep(2)
            response = map_client.places_nearby(
                location=(coord1, coord2),
                keyword=search_string,
                radius=distance,
                page_token=next_page_token
            )
            business_list.extend(response.get('results'))
            next_page_token = response.get('next_page_token')

        for x in business_list:
            st.info("**{0}** \n {1}".format(x["name"], x["vicinity"]))
