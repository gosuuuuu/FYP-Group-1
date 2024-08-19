import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
import base64

st.set_page_config(layout="wide",
                   initial_sidebar_state="collapsed",
                   page_title='IdentiLog'
                   )

st.markdown("<h1 style='text-align: center; color: black; background-color: #b8ffbc'>I D E N T I L O G</h1>", 
            unsafe_allow_html=True)

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

if menu == 'home':

    text1 = st.text_input("Just type anything and I will try to do when I come back to you guys")
    st.write(f"My text: {text1}")






if menu == 'upload':

    classes=["tidyman", "plastic_PS", "plastic_PP",
            "plastic_PET", "plastic_PAP", "plastic_other",
            "plastic_LDPE", "plastic_HDPE", "period_36m",
            "period_24m", "period_12m", "period_6m",
            "period_3m", "period_9m", "mobius_logo", "fsc",
            "ce_marking", "aluminium"] # 18 classes

    st.write('pog')
    menu_2 = option_menu(None, ["one", "multiple"], 
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
    if menu_2 == "one":
        upload_one = st.file_uploader('Upload Image For Logo Detection', type='jpg')
    elif menu_2 == "multiple":
        upload_multiple = st.file_uploader('Upload Image For Logos Detection', type='jpg')


        
    # Creating functions:
    def load_model():
        model = tf.keras.models.load_model('D:\Data Related Stuffs\FYP Model\FYP-Group-1\ResNet50.h5')
        return model

    def load_img (uploaded_file):
        img = Image.open(uploaded_file)
        img = img.resize((224,224))
        img_array = np.array(img)
        img_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)
        img_tensor = img_tensor/255.0
        img_tensor = tf.expand_dims(img_tensor,
                                    axis=0)
        return img_tensor

    # Main function
    def model_upload(submit_button):
        if submit_button:
            model = load_model()
            tensor = load_img(submit_button)
            # Upload_one
            prediction = model.predict(tensor)
            # Upload_multiple - detect number of cropped images
            prediction = model.predict(tensor)
            pred_class = classes[np.argmax(prediction)]
            st.write("predicted class:", pred_class)
    