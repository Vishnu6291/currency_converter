# Install generative AI package 
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# Initialize the model (Gemini 1.5 Turbo or Gemini Pro)
model = genai.GenerativeModel("gemini-2.5-flash")
# Initialize streamlit package
st.title("Welcome to your personal currency calculator")
st.header("Currency conversion just become easy")
name = st.text_input("May I know your name")
st.write(f"Hey, {name}")
option1 = st.selectbox ("Select the currency you want to convert", ["$", "€", "¥", "₹"])
option2 = st.selectbox ("Select the currency in which you want to convert", ["$", "€", "¥", "₹"])
amount = st.number_input("Enter the amount you want to convert")
# confirm user inputs
print(f"You selected: {option1} to convert in {option2}")
# Prompt generation
if st.button("Press for Result"):
    prompt = f"Act like an expert financial analyst, convert {option1} to {option2} for the amoount {amount}, give a fifty words commentary on the perfromance of currency {option1} in relation to {option2}"
    response = model.generate_content(prompt)
    st.markdown(response.text) # Comprehend markdowns in AI generated text