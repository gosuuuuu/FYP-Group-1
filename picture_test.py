import streamlit as st
from PIL import Image
import os

def save_image(image, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    image.save(os.path.join(path, filename))
    
st.write('test')

uploading = st.file_uploader('Please upload a file')
if uploading is not None:
    image = Image.open(uploading)
    save_path = "G:\My Drive\FYP Photos"

    save_image(image, save_path, uploading.name)
    st.image(image)
    