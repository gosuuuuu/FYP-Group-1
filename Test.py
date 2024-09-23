# Import Libraries
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from logo_identifier import LogoClassfier
from streamlit_cropper import st_cropper
from streamlit_modal import Modal

# Configuring the page layout
st.set_page_config(layout="wide",
                   initial_sidebar_state="collapsed",
                   page_title='IdentiLog'
                   )

# Setting the size and font of text
def black_font():
    st.markdown(
        """ <style>
        * {color: black !important;
            font-size: 21px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
black_font()

# Set Logo using URL
def set_logo(logo_url):
    st.markdown(
        f"""
        <div style="text-align:center;">
             <img src="{logo_url}" alt="Logo" style="width:300px;">
        </div>
        """,
        unsafe_allow_html=True
    )
logo_url = "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Logo%20and%20Background/BlackFontBG.png"
set_logo(logo_url)

# Set BG using URL 
def set_bg(img_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({img_url});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
img_url = "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Logo%20and%20Background/Background%20.png"
set_bg(img_url)

# Custom CSS for top navigation bar styling
st.markdown("""<style>
    body {
        margin: 0;
        padding: 0;
    }
    .top-bar {
        background-color: #80ed99;
        padding: 0;
        margin: 0;
        position: fixed;
        top: 80px;
        left: 0;
        right: 0;
        width: 100%;
        height: 70px;
        z-index: 1000;
        border-bottom: 2px solid #e0e0e0;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .top-bar a {
        padding: 15px;
        text-decoration: none;
        color: #000;
        font-weight: bold;
        flex: 1;
        text-align: center;
    }
    .top-bar a:hover {
        color: #DAD7CD;
    }
    .container {
        margin-top: 110px;
        padding: 20px;
    }
    .logo {
        text-align: center;
        margin-top: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Top navigation bar
st.markdown("""<div class="top-bar">
        <a href="?page=home">Home</a>
        <a href="?page=upload-prediction">Upload logo prediction</a>
        <a href="?page=description">Description</a>
        <a href="?page=recycle-logos">Recycle Logos</a>
    </div>
""", unsafe_allow_html=True)

# Get the query parameters
query_params = st.query_params
page = query_params.get("page", "home")

# Content for each page
if page == "home":
    st.title("Home")
    st.write("Welcome to the Home page!")

elif page == "upload-prediction":
    st.title("Upload Logo Prediction")
    st.write("Upload your logo for prediction.")

elif page == "description":
    st.title("Description")
    st.write("This is the description page.")

elif page == "recycle-logos":
    st.title("Recycle Logos")
    st.write("Information about recycling logos.")

# Additional container styling
st.markdown('<div class="container">', unsafe_allow_html=True)

# Home Page
if page == 'home':
    tab1, tab2 = st.tabs(['Description', 'Recycle Logos'])

    with tab1:  # Description Tab
        st.title("This is the Description tab.")
        st.write("Recycling symbols are used to help us identify different types of packaging and if they are capable of being recycled. "
                  "They can be confusing, so we are here to help you make sense of them and hopefully increase what you recycle in and out of the home.")

    with tab2:  # Recycle Logos Tab
        st.title("This is the Recycle Logos tab")
        st.write("Few logos that included in the project")
        # ... [rest of the content for the recycle logos tab] ...

# Handle different pages dynamically based on the navigation bar
if page == "home":
    st.title("Home")
    st.write("Welcome to the Home page!")

elif page == "upload-prediction":
    st.title("Upload Logo Prediction")
    st.write("Upload your logo for prediction.")
    
    # Add your custom modal and image upload logic here
    modal = Modal("Upload Modal")
    if modal.is_open():
        st.write("Modal content here.")

elif page == "description":
    st.title("Description")
    st.write("This is the description page.")

elif page == "recycle-logos":
    st.title("Recycle Logos")
    st.write("Information about recycling logos.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/aluminium.png", width=200)
        st.write("Aluminium Logo")
    
    with col2:
        st.write("This is a highly recyclable material.")

# Ensure the container styling applies
st.markdown('<div class="container">', unsafe_allow_html=True)