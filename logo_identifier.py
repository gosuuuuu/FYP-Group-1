import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import os
from PIL import Image
from streamlit_img_label import st_img_label
from streamlit_img_label.manage import ImageManager, ImageDirManager
from streamlit_cropper import st_cropper


class LogoClassfier:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.classes = ["tidyman", "plastic_PS", "plastic_PP",
                        "plastic_PET", "plastic_PAP", "plastic_other",
                        "plastic_LDPE", "plastic_HDPE", "period_36m",
                        "period_24m", "period_12m", "period_6m",
                        "period_3m", "period_9m", "mobius_logo", "fsc",
                        "ce_marking", "aluminium"] # 18 classes
    
    def logo_description(self, pred_class):
        if pred_class == "tidyman":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image') # To insert captured image
                with col_logo[1]:   
                    st.write('actual logo of prediction') # Insert predicted logo
            with st.container():
                st.write('description') # To insert description
            with st.container():
                st.write('steps on how to recycle / dispose material') # Insert steps
                
        elif pred_class == "plastic_PS":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "plastic_PP":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "plastic_PET":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')

        elif pred_class == "plastic_PAP":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "plastic_other":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "plastic_LDPE":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "plastic_HDPE":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "period_36m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "period_24m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "period_12m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "period_9m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "period_6m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "period_3m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "mobius_logo":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "fsc":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "ce_marking":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        elif pred_class == "aluminium":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.write('captured image')
                with col_logo[1]:   
                    st.write('actual logo of prediction') 
            with st.container():
                st.write('description') 
            with st.container():
                st.write('steps on how to recycle / dispose material')
        
        else:
            st.write('Logo undetected! Please try again.')
            st.write('List of logos that can be detected:')
            st.write('...') # To make list
        
    def load_img (self, uploaded_file):
        img = Image.open(uploaded_file)
        img = img.resize((224,224))
        img_array = np.array(img)
        img_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)
        img_tensor = img_tensor/255.0
        img_tensor = tf.expand_dims(img_tensor,
                                    axis=0)
        return img_tensor
    
    def model_upload(self, submit_button, menu_2):
        if submit_button:
            tensor = self.load_img(submit_button)
            if menu_2 == "one":
                prediction = self.model.predict(tensor)
            
            # Upload_multiple - detect number of cropped images
            elif menu_2 == "multiple":
                prediction = self.model.predict(tensor)
            
            pred_class = self.classes[np.argmax(prediction)]
            st.write("predicted class:", pred_class)
            
    # add function for crop here?