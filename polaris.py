import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Polaris"

)
st.title = ("Polaris")
st.header("Polaris")
st.subheader("The Hobby App")

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


st.text("Where do you live?")
lat = st.text_input("Latitude")
lon = st.text_input("Longitude")

if lat and lon:
    df = pd.DataFrame({
    'lat' : [float(lat)],
    'lon':[float(lon)],})
    st.dataframe(df)
    st.map(df)
    st.success("Map Successfully formed")


else:st.error("Warning, empty or invalid coordinates")



options = st.multiselect(
     'What do you like?',
     (['Sports', 'Gaming', 'Art', 'Music', 'Reading', 'Partying']))
if options:
 st.write('You like:', options)
