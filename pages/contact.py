import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='contact_form'):
    user_email = st.text_input("Enter your email address")
    user_message = st.text_area("Type in your message")
    message = f"""\
Subject: New request from {user_email}

From: {user_email}
{user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Thank you! Received your request, I will get back to you soon!")
