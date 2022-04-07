import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Polaris",
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
st.write("Please fill out the interests form on the top left menu to get started.")

coord1 = None
coord2 = None

# Hobbies/Interests Questionnaire
with st.sidebar:
    agree = st.checkbox('Do you agree to submit your personal information to this application?')
    if agree:
        st.write("Enter your name")
        first_name = st.text_input('First Name')
        last_name = st.text_input('Last Name')
        # Location section
        st.write("Where do you live?")
        col1, col2 = st.columns(2)
        with col1:
            coord1 = st.text_input("Latitude")
        with col2:
            coord2 = st.text_input("Longitude")

        hobby = st.radio(
            "Do you consider your hobbies extroverted or introverted?",
            ('Extroverted', 'Introverted'))
        if hobby == 'Extroverted':
            values = st.slider(
                'How extroverted are you on a scale of 1-10?',
                0.0, 10.0, 5.0)
        if hobby == "Introverted":
            values = st.slider(
                'How introverted are you on a scale of 1-10?',
                0.0, 10.0, 5.0)
        st.write('You are:', values, hobby)

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
    st.subheader("Map")
    if coord1 and coord2:
        df = pd.DataFrame({
            'lat': [float(coord1)],
            'lon': [float(coord2)], })
        st.dataframe(df)
        st.map(df)
        st.success("Map Successfully formed")
    else:
        st.error("Empty or invalid coordinates!")

with col4:
    # Displaying Locations/Events/Addresses
    st.subheader("Locations")
