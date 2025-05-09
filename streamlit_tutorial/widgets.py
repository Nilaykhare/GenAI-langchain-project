import streamlit as st
import pandas as pd


st.title("Streamlit input")
name = st.text_input("Enter your name")

age = st.slider("Select your age:",0,100,25)
options = ["python","java","js","c"]
choice = st.selectbox("Select your favourite programming language",options)

if name:
    st.write(f"Hello, {name}")
st.write(f"Your age is {age}")
st.write(f"Your favourite programming language is {choice}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
