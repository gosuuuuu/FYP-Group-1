import streamlit as st
import pandas as pd
import tensorflow as tf

st.set_page_config(layout="wide",
                   initial_sidebar_state="collapsed",
                   page_title='Testing saja'
                   )
st.markdown("<h1 style='text-align: center; color: black;'>sabar</h1>", unsafe_allow_html=True)


loaded_model = tf.keras.models.load_model('D:\Data Related Stuffs\FYP Model\FYP-Group-1\ResNet50.h5')

st.camera_input('test')