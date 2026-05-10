
import streamlit as st

# Basic Page Configuration
st.set_page_config(page_title="System Intelligence Test", layout="centered")

# App Content
st.title("🚀 System Intelligence: Space Test")
st.write("Welcome to your first app hosted on Deta Surf.")

# Simple Interaction
name = st.text_input("Enter your name to test the app:")
if name:
    st.success(f"Hello {name}! Your System Intelligence app is running perfectly.")

st.info("This is a live test of Streamlit on Deta Space.")
