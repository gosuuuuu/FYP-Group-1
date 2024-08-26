import streamlit as st

# Set page configuration
st.set_page_config(page_title="Top Sidebar Example", layout="wide")

# Custom CSS for top "sidebar" styling
st.markdown("""
    <style>
    .top-bar {
        background-color: #588157;
        padding: 0;
        margin: 0;
        position: fixed;
        top: 0.5;
        left: 0;
        right: 0;
        width: 100%;
        z-index: 9999;
        border-bottom: 2px solid #e0e0e0;
        display: flex;
        justify-content: space-around;
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
        margin-top: 60px;  /* Offset for the top bar */
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Top "sidebar"
st.markdown("""
    <div class="top-bar">
        <a href="?page=home">Home</a>
        <a href="?page=upload">Upload</a>
        <a href="?page=description">Description</a>
        <a href="?page=recycle-logos">Recycle Logos</a>
        <a href="?page=contact">Contact</a>
    </div>
""", unsafe_allow_html=True)

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
    st.write("Contact us here.")

# Additional container styling
st.markdown('<div class="container">', unsafe_allow_html=True)
