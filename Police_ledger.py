import pandas as pd
import streamlit as st

st.title(" Title !!!!!!!!!!")
st.header("Hello Header \\\\\\\\////////")
st.write("This is just a test .................")

name = st.text_input("Share your Name ->")
if name: st.success(f"Hello {name}, Welcome ==>>")

age = st.slider("Select Your Age :-",0,200)
st.write(f"Your age is {age}")