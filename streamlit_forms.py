import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# title
st.title("Streamlit Form Demo")

# form to hold the interactive elements
with st.form(key="sample_form"):

    # text input
    st.subheader("Text Input")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Enter your feedback")

    # date and time input
    st.subheader("Date and Time Input")
    dob = st.date_input("Enter your date of birth")
    time = st.time_input("Choose a prefered time")

    # selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["Option1", "Option2", "Option3"])
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5])

    # toggles and checkboxes
    st.subheader("Toggles and Checkboxes")
    notifications = st.checkbox("Receive notifications?")
    toogle_value = st.toggle("Enable dark mode?", value=False)

    # submit button for the form
    submit_button = st.form_submit_button(label="Submit")