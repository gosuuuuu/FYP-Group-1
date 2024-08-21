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

st.set_page_config(layout="wide",
                   initial_sidebar_state="collapsed",
                   page_title='IdentiLog'
                   )

# To be changed
st.markdown("<h1 style='text-align: center; color: black; background-color: #b8ffbc'>I D E N T I L O G</h1>", 
            unsafe_allow_html=True)


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

img_bg = r"C:\Users\User\OneDrive\Desktop\identilog_bg.jpg"
set_bg(img_bg)


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

    text1 = st.text_input("Just type anything and I will try to do when I come back to you guys")
    st.write(f"My text: {text1}")

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

    st.write('Upload file') # To insert description
    upload = st.file_uploader('Upload Image For Logo Detection', type='jpg')
    
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
    
    st.write('test for cropper')
    
    if upload:
        img = Image.open(upload)
        
        with st.form('Number Form'):
            number_of_logos = st.number_input('How Many Logos To Detect?',
                                            min_value = 1,
                                            step = 1,
                                            )
            submit = st.form_submit_button('Submit')
            
        cropped_img_list = []
        
        for index in range(number_of_logos):
            cropped_image = st_cropper(img,
                                    realtime_update = False,
                                    aspect_ratio = None,
                                    key = index)
            cropped_img_list.append(cropped_image)    
        done = st.checkbox('Done!')
        
        if done:
            st.empty()
            for cropped_image in cropped_img_list:
                with st.container(border=True):
                    column = st.columns(2)
                    with column[0]:
                        cropped_image = cropped_image.resize((100,100))
                        st.image(cropped_image)
                    with column[1]:
                        st.write('insert information')