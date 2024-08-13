import streamlit as st
import pandas as pd
import tensorflow as tf

st.title('Identilog')
st.write('Identilog')

st.camera_input('test')

text1 = st.text_input("Just type anything and I will try to do when I come back to you guys")
st.write(f"My text: {text1}")

