import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
import base64
from logo_identifier import LogoClassfier
from streamlit_img_label import st_img_label
from streamlit_cropper import st_cropper
import os
from streamlit_modal import Modal
import streamlit.components.v1 as components

st.set_page_config(layout="wide",
                   initial_sidebar_state="collapsed",
                   page_title='IdentiLog'
                   )

# To be changed
#st.markdown("<h1 style='text-align: center; color: black; background-color: #b8ffbc'>I D E N T I L O G</h1>", 
            #unsafe_allow_html=True)

#################### LOGO ####################

def set_logo(logo_path):
    
    with open(logo_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <div style="text-align:center;">
             <img src="data:image/png;base64,{encoded_string}" alt="Logo" style="width:300px;">
        </div>
        """,
        unsafe_allow_html=True
    )

logo_path = r"C:\Users\insya\Desktop\Black_BG.png"
set_logo(logo_path)

# Ena - Saya comment dulu pasal ada error
# If can kalau dapat insert logo into the file instead of makai path

#logo_path_aina = r"C:\Users\User\OneDrive\Desktop\identilog_logo.jpg"
#set_logo(logo_path_aina)

#################### BACKGROUND IMAGE ####################
def set_bg(img_path):
    bg_ext = 'png'
    
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{bg_ext};base64,{encoded_string})
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# img_bg = r"C:\Users\bayan\OneDrive\Desktop\2.png"
# set_bg(img_bg)

img_bg = r"C:\Users\insya\Pictures\Wallpaper\Lock Screen.jpg"
set_bg(img_bg)

#img_bg_ena = r"C:\Users\User\OneDrive\Desktop\identilog_bg.jpg"
#set_bg(img_bg_ena)


#################### OPTION MENU ####################
menu = option_menu(None, ["home", "upload"], 
    icons=['house', 'cloud-upload'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", 
                        "background-color": "#cfffdd"},
        "icon": {"color": "green", 
                    "font-size": "20px"}, 
        "nav-link": {"font-size": "14px",
                        "font-family": "arial" , # to be changed
                        "text-align": "center", 
                        "margin":"0px", 
                        "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#19c24a"}
    }
)

# Home Page
if menu == 'home':
    tab1, tab2, tab3 = st.tabs(['Description', 'Recycle Logos', 'Contact'])

    with tab1:
        st.write("This is the Description tab.")

    with tab2:
        st.write("This is the Recycle Logos tab.")

    with tab3:

        st.header(":envelope: Get In Touch With Us!")

        import streamlit as st

        contact_form = """
            <style>
            form {
                width: 100%;
            }
            input[type=text], input[type=email], textarea {
                width: 100%;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
                margin-top: 6px;
                margin-bottom: 16px;
            }
            textarea {
                resize: vertical;
            }
            button[type=submit] {
                background-color: #04AA6D;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button[type=submit]:hover {
                background-color: #45a049;
            }
            </style>
            <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here"></textarea>
                <button type="submit">Send</button>
            </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

# insert description of website
# how to use upload function steps
# table of contents with links


# Upload Page
if menu == 'upload':
    # 18 classes of logo
    classes=["tidyman", "plastic_PS", "plastic_PP",
            "plastic_PET", "plastic_PAP", "plastic_other",
            "plastic_LDPE", "plastic_HDPE", "period_36m",
            "period_24m", "period_12m", "period_6m",
            "period_3m", "period_9m", "mobius_logo", "fsc",
            "ce_marking", "aluminium"]

    st.write('Insert description or text here') # To insert description
    
    
    
# Main Function with Modal

    # Creating modals
    modal_number_logos = Modal("Number Of Logos And File",
                               key = 'modal 1',
                               max_width=800
    )

    # Initializing sessions
    if 'uploaded_img' not in st.session_state:
        st.session_state.uploaded_img = None
    if 'number_logos' not in st.session_state:
        st.session_state.number_logos = 2
    if 'cropped_img_list' not in st.session_state:
        st.session_state.cropped_img_list = []

    # Button
    with st.container():
        open_modal = st.button("Open",
                               use_container_width=True,
                               help='To upload image')
        if open_modal:
            modal_number_logos.open()

    if modal_number_logos.is_open():
        with modal_number_logos.container():
            st.session_state.number_logos = st.number_input('Insert',
                                           min_value=1,
                                           step=1)
            st.session_state.uploaded_img = st.file_uploader('Insert File here')
            done = st.button('done',
                               use_container_width=True)
        if done:
            modal_number_logos.close()    
        
    if st.session_state.uploaded_img is not None:
        img = Image.open(st.session_state.uploaded_img)
        st.session_state.cropped_img_list = []
        crop_section = st.empty()
        
        with crop_section.container():
            st.write('Double click on image to save image for crop!')
            for index in range(st.session_state.number_logos):
                cropped_image = st_cropper(img,
                                        realtime_update = False,
                                        aspect_ratio = None,
                                        key = index)
                st.session_state.cropped_img_list.append(cropped_image)    
            show_img = st.button('Done Cropping !')
        
        if show_img:
            crop_section.empty()
            display_section = st.empty()
            my_prediction = LogoClassfier('D:\Data Related Stuffs\FYP Model\FYP-Group-1\ResNet50.h5')
            
            with display_section.container():
                for cropped_image in st.session_state.cropped_img_list:
                    loaded_img = my_prediction.load_img(cropped_image)
                    
                    with st.container(border=True):
                        pred_class = my_prediction.model_upload(loaded_img)       
    
    else:
        st.write('Please upload an image.')

    #         html_string = '''
    #         <h1>HTML string in RED</h1>

    #         <script language="javascript">
    #         document.querySelector("h1").style.color = "red";
    #         </script>
    #         '''
    #         components.html(html_string)

    #         st.write("Some fancy text")
    #         value = st.checkbox("Check me")
    #         st.write(f"Checkbox checked: {value}")
    
    
    # To uncomment once crop is done
#     menu_2 = option_menu(None, ["one", "multiple"], 
#     icons=['house', 'cloud-upload'],
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", 
#                         "background-color": "#cfffdd"},
#         "icon": {"color": "green", 
#                     "font-size": "20px"}, 
#         "nav-link": {"font-size": "14px",
#                         "font-family": "arial" , # to be changed
#                         "text-align": "center", 
#                         "margin":"0px", 
#                         "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "#19c24a"}
#     }
# )
#     if menu_2 == "one":
#         upload_one = st.file_uploader('Upload Image For Logo Detection', type='jpg')
#     elif menu_2 == "multiple":
#         upload_multiple = st.file_uploader('Upload Image For Logos Detection', type='jpg')
    
    
    # Using Class LogoClassfier from created file
    # my_prediction = LogoClassfier('D:\Data Related Stuffs\FYP Model\FYP-Group-1\ResNet50.h5')
