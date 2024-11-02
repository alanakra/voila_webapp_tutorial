import streamlit as st

st.title("Welcome Home!")
st.write("This is a WebApp demo")
a = st.number_input('How much do you love this demo?')
st.write("Value: ", a)

w = st.file_uploader("Upload a CSV file", type="csv")
if w:
    import pandas as pd

    data = pd.read_csv(w)
    st.write(data)