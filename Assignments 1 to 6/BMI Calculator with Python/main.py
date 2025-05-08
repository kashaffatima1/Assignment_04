# Task : 8
# BMI Calculator with Python & Streamlit

import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 200, 170)
width = st.slider("Enter your weight (in kg):", 30, 100, 80)

bmi = round(width / ((height / 100) ** 2))
st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- Underwight: BMI less than 18.5")
st.write("- Normal weightL BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9 ")
st.write("- Obesity: BMI 30 or greater")
