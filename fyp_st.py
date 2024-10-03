# Import Libraries
import streamlit as st
import os
from PIL import Image
from streamlit_option_menu import option_menu
from logo_identifier import LogoClassfier
from streamlit_cropper import st_cropper
from streamlit_modal import Modal
from datetime import datetime as dt

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
        <div style="text-align:center; margin-top: -60px;">
             <img src="{logo_url}" alt="Logo" style="width:250px;">
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


#################### OPTION MENU ####################
menu = option_menu(None, ["Home", "Upload Logo Prediction"], 
    icons=['house', 'cloud-upload'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", 
                        "background-color": "#cfffdd"},
        "icon": {"color": "green", 
                    "font-size": "20px"}, 
        "nav-link": {"font-size": "20px",
                        "font-family": "arial" , # to be changed
                        "text-align": "center", 
                        "margin":"0px", 
                        "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#19c24a"}
    }
)

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

query_params = st.query_params
page = query_params.get("page", "home")

# Home Page
if page == "home":
    st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Logo%20and%20Background/classic-removebg-preview.png" 
                        width="1430">
                </div>
                """,
                unsafe_allow_html=True,
            )


elif page == "description":
    st.title("This is the Description tab. \n")
    st.write("Recycling symbols are used to help us identify different types of packaging and if they are capable of being recycled.  \n"
        "They can be confusing, so we are here to help you make sense of them and hopefully increase what you recycle in and out of the home.")
    
elifyy
    st.title("This is the Recycle Logos tab \n")
    st.write("Few logos that included in the project")

    col1, col2, col3, col4 = st.columns([3,6,3,6])

    with col1:
        st.markdown(
            """
            <div style='text-align: center; margin: 0px 100px 50px 0px;'>
                <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/aluminium.png" 
                    alt="Aluminium Logo" 
                    width="180">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.subheader("Aluminium")
        st.markdown(
        """
        <p style='font-size:100px;'>
        ALU: Represents aluminum, which can be recycled at The Green Depot in Kuala Belait but typically requires specialized processing. Recycling aluminum helps reduce energy consumption and environmental impact. For more information, visit The Green Depot.
        </p>
        """,
        unsafe_allow_html=True,
        )
        st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn")

    with col3:
        st.markdown(
            """
            <div style='text-align: center; margin: 0px 100px 50px 0px;'>
                <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/ce.png"  
                    width="230">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.subheader("CE")
        st.write(
            """
            This indicates conformity with health, safety, and environmental protection standards for products sold within the European Economic Area.  
            """
        )

    col5, col6, col7, col8 = st.columns([3,6,3,6])

    with col5:
        st.markdown(
            """
            <div style='text-align: center; margin: 0px 100px 50px 0px;'>
                <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/fsc.png" 
                    width="170">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col6:
        st.subheader("FSC")
        st.write(
            """
            This certifies that the wood or paper products come from responsibly managed forests. it can be recycled at The Green Depot.   
            """
        )
        st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn")
        
    with col7:
        st.markdown(
            """
            <div style='text-align: center; margin: 0px 100px 50px 0px;'>
                <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/mobiusloop.png" 
                    width="180">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col8:
        st.subheader("Mobius Loop")
        st.write(
            """
            This symbol indicates recyclability, though whether a product can be recycled easily depends on local facilities. In Brunei, it may require specialized facilities like The Green Depot.   
            """
        )
        st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn")

    col9, col10, col11, col12 = st.columns([3,6,3,6])

    with col9:
        st.markdown(
            """
            <div style='text-align: center; margin: 0px 100px 50px 0px;'>
                <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png"  
                    width="200">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col10:
        st.subheader("Period After Opening")
        st.write(
            """
            The period-after-opening (PAO) symbol highlights the amount of time a cosmetic product will remain safe for use after being opened for the first time. It depicts an open cosmetics pot and is used together with a written number of months or years.  
            """
        )

    with col11:
        st.markdown(
            """
            <div style='text-align: center; margin: 0px 100px 50px 0px;'>
                <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                    width="200">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col12:
        st.subheader("Plastic")
        st.write(
            """
            These symbols help consumers to identify different types of plastic resin used to make the product.They were applied to help assist with the sorting of plastics. Like many materials plastics should be recycled separately, so the value of the of the recycled material is preserved. Allowing it to be reused to make new products.  
            """
        )

    col13, col14, col15, col16 = st.columns([3,6,3,6])

    with col13:
        st.markdown(
            """
            <div style='text-align: center; margin: 0px 100px 50px 0px;'>
                <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/tidyman.png" 
                    width="180">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col14:
        st.subheader("Tidyman")
        st.write(
            """
                This symbol is a reminder to dispose of waste responsibly. It encourages consumers to throw their trash into appropriate trash cans, helping to keep the environment clean. While not a recycling logo, it promotes good waste management practices.  
            """
        )


# Upload Page
if menu == 'Upload Logo Prediction':
    my_prediction = LogoClassfier("G:\My Drive\Poli\SEM 5\ResNet50.h5") # Change to google drive
    
    # 18 classes of logo
    classes=["tidyman", "plastic_PS", "plastic_PP",
            "plastic_PET", "plastic_PAP", "plastic_other",
            "plastic_LDPE", "plastic_HDPE", "period_36m",
            "period_24m", "period_12m", "period_6m",
            "period_3m", "period_9m", "mobius_logo", "fsc",
            "ce_marking", "aluminium"]

    st.header('Do you want to know how to dispose of your rubish? We can help you with that.\n') # To insert description
    st.write('Find any recycle logo on your items and upload it!\n')

# Modal
    # Creating Modal
    modal_number_logos = Modal("Number Of Logos And File",
                               key='modal 1',
                               max_width=800
    )

    # Initializing sessions
    if 'uploaded_img' not in st.session_state:
        st.session_state.uploaded_img = None
    if 'number_logos' not in st.session_state:
        st.session_state.number_logos = 2
    if 'cropped_img_list' not in st.session_state:
        st.session_state.cropped_img_list = []
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False 
    

    # Button
    with st.container():
        open_modal = st.button("Ready to upload!",
                               use_container_width=True,
                               help='To upload image')
        if open_modal: # If button is clicked
            modal_number_logos.open()

    if modal_number_logos.is_open(): # When the variable is opened
        with modal_number_logos.container():
            st.session_state.number_logos = st.number_input('Insert how many recycle logos you want to know',
                                           min_value=1,
                                           step=1)
            st.session_state.uploaded_img = st.file_uploader('Insert File here into "Browse files"')
            st.write('Click "Done insert" if you are done inserting')
            done_button = st.button('Done insert!',
                               use_container_width=True)
        if done_button:
            modal_number_logos.close() # Modal page is closed    
        
    if st.session_state.uploaded_img is not None:
        img = Image.open(st.session_state.uploaded_img)
        st.session_state.cropped_img_list = []
        
        # Crop section
        crop_section = st.empty()
        with crop_section.container():
            st.write('Double click on image to save image for crop!')
            for index in range(st.session_state.number_logos):
                cropped_image = st_cropper(img,
                                        realtime_update = False,
                                        aspect_ratio = None,
                                        key = index)
                st.session_state.cropped_img_list.append(cropped_image)
            
            
            def save_image(images, path, filename=None):
                if not os.path.exists(path):
                    os.makedirs(path)
                
                for index, image in enumerate(images):
                    filename = f"image_{dt.now().strftime('%d%m%Y_%H%M')}_{index}.png"
                    image.save(os.path.join(path, filename))
                
            show_img = st.button('Done Cropping !')
            save_path = "G:\My Drive\FYP Photos"
            save_image(st.session_state.cropped_img_list, save_path)
        
        # Display section
        if show_img:
            st.session_state.uploaded_img = None
            crop_section.empty()
            display_section = st.empty()
        
            with display_section.container():
                for cropped_image in st.session_state.cropped_img_list:
                    loaded_img = my_prediction.load_img(cropped_image)
                    
                    with st.container(border=True):
                        pred_class = my_prediction.model_upload(cropped_image, loaded_img)
            
        
else:
    st.write('Please upload an image.')

menu2 = option_menu(None, ["Recycle", "Upload Logo Prediction"],)
if menu2 == 'Recycle':
    st.markdown(
        st.title("Recyle"))
                