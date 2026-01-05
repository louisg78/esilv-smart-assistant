import streamlit as st
from agents.orchestrator import orchestrate
from agents.form_agent import collect_contact_info
import pandas as pd
import os

st.set_page_config(page_title="ESILV Smart Assistant")

# ----- SESSION STATE -----
if 'login' not in st.session_state:
    st.session_state.login = False
if 'role' not in st.session_state:
    st.session_state.role = None
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'show_form' not in st.session_state:
    st.session_state.show_form = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# ----- LOGIN PAGE -----
CREDENTIALS = {"admin": "admin123", "student": "student123"}

if not st.session_state.login:
    st.title("🎓 ESILV Smart Assistant Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in CREDENTIALS and password == CREDENTIALS[username]:
            st.session_state.login = True
            st.session_state.role = username
            st.success(f"Logged in as {username}")
        else:
            st.error("Invalid username or password")
    st.stop()  # stop here until login is successful

# ----- MAIN CHAT PAGE -----
st.title("🎓 ESILV Smart Assistant")
st.write("Ask questions about ESILV or register for programs.")

# Chat input
user_input = st.text_input("Type your message here:")

# Handle input
if user_input:
    if any(word in user_input.lower() for word in ["register", "contact", "sign up", "follow up"]):
        st.session_state.show_form = True
        st.session_state.conversation.append(("You", user_input))
    else:
        with st.spinner("Searching ESILV knowledge base..."):
            reply = orchestrate(user_input)
        st.session_state.conversation.append(("You", user_input))
        st.session_state.conversation.append(("ESILV Assistant", reply))

# ----- DISPLAY REGISTRATION FORM -----
if st.session_state.show_form and not st.session_state.form_submitted:
    st.write("Please provide your details:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    interest = st.text_input("Program Interest")
    if st.button("Submit"):
        reply = collect_contact_info(name, email, interest)
        st.session_state.conversation.append(("ESILV Assistant", reply))
        st.session_state.form_submitted = True
        st.session_state.show_form = False

# ----- DISPLAY CHAT -----
for speaker, message in st.session_state.conversation:
    st.markdown(f"**{speaker}:** {message}")

# ----- ADMIN VIEW -----
st.markdown("---")
if st.session_state.role == "admin":
    if st.checkbox("Show all registered contacts (admin)"):
        if os.path.exists("contacts.csv"):
            contacts_df = pd.read_csv("contacts.csv")
            st.dataframe(contacts_df)
        else:
            st.info("No contacts submitted yet.")
