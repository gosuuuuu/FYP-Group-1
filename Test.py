import streamlit as st

# Set Streamlit layout to wide
st.set_page_config(layout="wide")

# Initialize session state for page selection if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Define the HTML for the navigation bar
st.markdown("""
    <style>
    /* Navigation bar styling */
    .topnav {
        background-color: #333; /* Dark background */
        width: 100vw; /* Full viewport width */
        position: fixed; /* Fix it to the top */
        top: 1; /* Align it to the top of the screen */
        left: 0; /* Align it to the left edge of the screen */
        z-index: 1000; /* Ensure it is above other content */
        display: flex;
        justify-content: center; /* Center the links */
        box-sizing: border-box; /* Ensure padding is included in width */
        padding: 10px 0; /* Add padding for better spacing */
    }

    .topnav button {
        color: white; /* White text */
        background-color: #333; /* Dark background */
        border: none;
        padding: 14px 20px;
        font-size: 17px;
        cursor: pointer;
        margin: 0 5px; /* Space between buttons */
        border-radius: 5px; /* Rounded corners */
    }

    .topnav button:hover {
        background-color: #ddd;
        color: black;
    }

    .topnav button.active {
        background-color: #04AA6D;
        color: white;
    }

    /* Ensure content is not hidden behind the nav bar */
    .main-content {
        margin-top: 70px; /* Adjust based on nav bar height */
    }
    </style>
    <div class="topnav">
        <button id="home-btn" onclick="location.href='?page=home'">Home</button>
        <button id="about-btn" onclick="location.href='?page=about'">About</button>
        <button id="contact-btn" onclick="location.href='?page=contact'">Contact</button>
    </div>
    <script>
    // Function to update the active button based on the URL query parameter
    function updateActiveButton() {
        const urlParams = new URLSearchParams(window.location.search);
        const page = urlParams.get('page') || 'home';
        document.querySelectorAll('.topnav button').forEach(button => {
            button.classList.remove('active');
        });
        const activeButton = document.querySelector(`#${page}-btn`);
        if (activeButton) {
            activeButton.classList.add('active');
        }
    }

    // Set the active button on page load and query parameter change
    window.addEventListener('load', updateActiveButton);
    window.addEventListener('popstate', updateActiveButton);
    </script>
    """, unsafe_allow_html=True)

# Handle page selection using Streamlit
query_params = st.query_params
if 'page' in query_params:
    st.session_state.page = query_params['page'][0]

# Main content
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

if st.session_state.page == "home":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
elif st.session_state.page == "about":
    st.title("About Page")
    st.write("This is the About Page!")
elif st.session_state.page == "contact":
    st.title("Contact Page")
    st.write("This is the Contact Page!")
else:
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

st.markdown("</div>", unsafe_allow_html=True)
