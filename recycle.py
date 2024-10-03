import streamlit as st

# Function for Page 1
def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")
    if st.button("Go to Page 2"):
        st.session_state.page = "Page 2"

# Function for Page 2
def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")
    if st.button("Go to Page 1"):
        st.session_state.page = "Page 1"

if 'page' not in st.session_state:
    st.session_state.page = "Page 1"

# Display pages based on session state
if st.session_state.page == "Page 1":
    page1()
else:
    page2()

# Initialize session state if it doesn't exist
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False

if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False

# Page layout
st.title("Button Display Example")

# First button
if st.button("Show Second Button"):
    st.session_state.button1_clicked = True

# Display second button if the first button is clicked
if st.session_state.button1_clicked:
    st.write("First button was clicked!")
    if st.button("Show Message"):
        st.session_state.button2_clicked = True

# Display a message if the second button is clicked
if st.session_state.button2_clicked:
    st.success("Second button was clicked! Here's your message.")

import streamlit as st

# Function for Page 1
def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

# Function for Page 2
def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")

# Initialize session state for page selection
if 'page' not in st.session_state:
    st.session_state.page = "Page 1"

# Sidebar or header buttons (always visible)
col1, col2 = st.columns(2)
with col1:
    if st.button("Page 1"):
        st.session_state.page = "Page 1"
with col2:
    if st.button("Page 2"):
        st.session_state.page = "Page 2"

# Display the content based on which button is clicked
if st.session_state.page == "Page 1":
    page1()
elif st.session_state.page == "Page 2":
    page2()
