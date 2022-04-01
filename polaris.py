import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Polaris",
    layout = "wide"

)
st.title = ("Polaris")
st.header("Polaris")
st.subheader("The Hobby App")
st.write("Please fill out the interests form on the top left menu to get started.")

# Hobbies/Interests Questionnaire
with st.sidebar:
    agree = st.checkbox ('Do you agree to submit your personal information to this application?')
    if(agree):
     st.text("Enter your name")
    first_name=st.text_input('First Name')
    last_name=st.text_input('Last Name')

    hobby = st.radio(
         "Do you consider your hobbies extroverted or introverted?",
         ('Extroverted', 'Introverted'))

    if hobby == 'Extroverted':
     st.text('How extroverted do you think you are on a scale of 1-10?')
     values = st.slider(
         'Select a range of values',
           0.0, 10.0, 5.0)

    if hobby =="Introverted":
     st.text("How introverted do you think you are on a scale of 1-10?")
     values = st.slider(
         'Select a range of values',
           0.0, 10.0, 5.0)
    st.write('You are:', values, hobby)

    options = st.multiselect(
        'What do you like?',
        (['Sports', 'Gaming', 'Art', 'Music', 'Reading', 'Partying']))
    if options:
        st.write('You like:', options)

# Location section
st.text("Where do you live?")
col1, col2 = st.columns(2)
with col1:
    lat = st.text_input("Latitude")
with col2:
    lon = st.text_input("Longitude")

col3, col4 = st.columns(2)
with col3:
    # Displaying the Map
    st.subheader("Map")
    if lat and lon:
        df = pd.DataFrame({
        'lat' : [float(lat)],
        'lon':[float(lon)],})
        st.dataframe(df)
        st.map(df)
        st.success("Map Successfully formed")


    else:st.error("Warning, empty or invalid coordinates")

with col4:
    #Displaying Locations/Events/Addresses
    st.subheader("Locations")



