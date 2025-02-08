import streamlit as st
import pandas as pd


# title
st.title("Streamlit Elements Demo")

# dataframe section
st.subheader("Dataframe")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 47],
    "Occupation": ["Engineer", "Doctor", "Artist", "Chef"]
})
st.dataframe(df)

# data editor section
st.subheader("Data Editor")
editable_df = st.data_editor(df)

# static table selection
st.subheader("Static Table")
st.table(df)

# metrics section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df["Age"].mean(), 1))

# json and dict section
st.subheader("JSON and Dictionary")
sample_dict = {
    "anme": "Alice",
    "age": 25,
    "skills": ["python", "data science", "machine learning"]
}
st.json(sample_dict)

# also show it as dictionary
st.write("Dictionary View:", sample_dict)