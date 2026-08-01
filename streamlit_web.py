import streamlit as st

st.title("Hello, Streamlit!")

name = st.text_input("StudentName", placeholder="Enter your name")
address = st.text_input("Address")
hsc_percentage = st.number_input("HSC Percentage", 0.0, 100.0)
roll_number = st.number_input("Roll Number", 1, 100)

submit_button = st.button("Submit")

# Backend
if submit_button:
    st.write("Data Submitted Successfully!")

    if not name:
        st.error("Please enter your name.")
    else:
        st.write(f"From Backend:-- Name: {name}")
        st.write(f"From Backend:-- Address: {address}")
        st.write(f"From Backend:-- HSC Percentage: {hsc_percentage}")
        st.write(f"From Backend:-- Roll Number: {roll_number}")
