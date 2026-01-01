import streamlit as st

st.set_page_config(page_title="Team 4 AI Project", page_icon="🚀")

st.title("Hello, TechSprint! 🚀")
st.write("This is our first collaborative AI App.")

# A simple interactive button
if st.button("Click me!"):
    st.success("Great job! The environment is set up correctly.")
    st.balloons()