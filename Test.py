import streamlit as st

# Set page configuration
st.set_page_config(page_title="Top Sidebar Example", layout="wide")

# Custom CSS for top navigation bar styling
st.markdown("""
    <style>
    body {
        margin: 0;
        padding: 0;
    }
    .top-bar {
        background-color: #80ed99;
        padding: 0;
        margin: 0;
        position: fixed;
        top: 60px;  /* Adjust this value based on header height */
        left: 0;
        right: 0;
        width: 100%;
        height: 50px; /* Set a fixed height for the navigation bar */
        z-index: 1000; /* Ensure it's above other elements */
        border-bottom: 2px solid #e0e0e0;
        display: flex;
        justify-content: space-around;
        align-items: center; /* Center items vertically */
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
        margin-top: 110px;  /* Adjust this to account for both the header and the top-bar */
        padding: 20px;
    }
    .logo {
        text-align: center;
        margin-top: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Top navigation bar
st.markdown("""
    <div class="top-bar">
        <a href="?page=home">Home</a>
        <a href="?page=upload">Upload</a>
        <a href="?page=description">Description</a>
        <a href="?page=recycle-logos">Recycle Logos</a>
        <a href="?page=contact">Contact</a>
    </div>
""", unsafe_allow_html=True)

# Set the background image
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

# Set the logo
def set_logo(logo_url):
    st.markdown(
        f"""
        <div class="logo">
             <img src="{logo_url}" alt="Logo" style="width:300px;">
        </div>
        """,
        unsafe_allow_html=True
    )

logo_url = "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Logo%20and%20Background/BlackFontBG.png"
set_logo(logo_url)

# Get the query parameters
query_params = st.query_params
page = query_params.get("page", "home")

# Content for each page
if page == "home":
    st.title("Home")
    st.write("Welcome to the Home page!")

elif page == "upload":
    st.title("Upload")
    st.write("Upload your files here.")

elif page == "description":
    st.title("Description")
    st.write("This is the description page.")

elif page == "recycle-logos":
    st.title("Recycle Logos")
    st.write("Information about recycling logos.")

elif page == "contact":
    st.title("Contact")
    st.write("You can reach us at contact@example.com")

# Additional container styling
st.markdown('<div class="container">', unsafe_allow_html=True)
