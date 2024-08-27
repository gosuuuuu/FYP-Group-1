# Import Libraries
import streamlit as st
import numpy as np
import tensorflow as tf
import base64
import io


class LogoClassfier:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.classes = ["tidyman", "plastic_PS", "plastic_PP",
                        "plastic_PET", "plastic_PAP", "plastic_other",
                        "plastic_LDPE", "plastic_HDPE", "period_36m",
                        "period_24m", "period_12m", "period_6m",
                        "period_3m", "period_9m", "mobius_logo", "fsc",
                        "ce_marking", "aluminium"] # 18 classes

    
    def load_img (self, img):
        img = img.resize((224,224))
        img_array = np.array(img)
        img_tensor = tf.convert_to_tensor(img_array, dtype=tf.float32)
        img_tensor = img_tensor/255.0
        img_tensor = tf.expand_dims(img_tensor,
                                    axis=0)
        return img_tensor
    
    
    def model_upload(self, cropped_image, loaded_img):
            prediction = self.model.predict(loaded_img)
            pred_class = self.classes[np.argmax(prediction)]

            if pred_class == "tidyman":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('A symbol encouraging proper waste disposal. ')
                with st.container():
                    st.write('as this symbol is to encourage the buyer , it is not applicable; this is not a recycling logo. therefore dispose of waste responsibly in the appropriate bin.  ') # Insert steps
                    
            elif pred_class == "plastic_PS":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('Often used for disposable cutlery and foam containers. It is not easily recyclable.') 
                with st.container():
                    st.write('As it is not easily recyclabl, You may Dispose of it in a general waste. ')
            
            elif pred_class == "plastic_PP":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('A Recycable plastic used for containers, straws, and some packaging.') 
                with st.container():
                    st.write('Rinse and place in the recycling bin. ')
            
            elif pred_class == "plastic_PET":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('A Recycable plastic used for containers, straws, and some packaging.') 
                with st.container():
                    st.write('steps on how to recycle / dispose material')

            elif pred_class == "plastic_PAP":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('Depends on local facilities it is recycable , it is used in various applications, including textiles and packaging. ') 
                with st.container():
                    st.write('If not recyclable, dispose of in general waste. ')
            
            elif pred_class == "plastic_other":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('Depends on the specific type; check local guidelines it is recycable. This logo covers various types of plastic that do not fit into the other categories.  ') 
                with st.container():
                    st.write('If not recyclable, dispose of in general waste. ')
            
            elif pred_class == "plastic_LDPE":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('Often used for plastic bags and some containers. Yes it is recycable, but only at specific facilities. ') 
                with st.container():
                    st.write('Take to grocery stores that accept plastic bags. ')
            
            elif pred_class == "plastic_HDPE":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('Commonly used for containers like milk jugs and detergent bottles. Yes, it is recycable ') 
                with st.container():
                    st.write('Rinse and place in the recycling bin. ')
            
            elif pred_class == "period_36m":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo indicates the product should be used within thirty-six months after opening. Depending on the material it is recycable') 
                with st.container():
                    st.write('steps on how to recycle / dispose material')
            
            elif pred_class == "period_24m":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo Indicates the product should be used within twenty-four months after opening. Depending on the material it is recycable') 
                with st.container():
                    st.write('Check specific material guidelines. ')
            
            elif pred_class == "period_12m":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo indicates the product should be used within twelve months after opening. Depending on the material it is recycable') 
                with st.container():
                    st.write('Check specific material guidelines. ')
            
            elif pred_class == "period_9m":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo indicates the product should be used within nine months after opening. Depending on the material it is recycable') 
                with st.container():
                    st.write('Check specific material guidelines. ')
            
            elif pred_class == "period_6m":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo indicates the product should be used within six months after opening. Depending on the material it is recycable') 
                with st.container():
                    st.write('Check specific material guidelines. ')
            
            elif pred_class == "period_3m":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo indicates the product should be used within three months after opening. Depending on the material it is recycable') 
                with st.container():
                    st.write('Check specific material guidelines.')
            
            elif pred_class == "mobius_logo":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo represents that the product is recyclable. ') 
                with st.container():
                    st.write('Check local guidelines for specific recycling instructions. ')
            
            elif pred_class == "fsc":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo certifies that the wood or paper products come from responsibly managed forests. It is recycable ') 
                with st.container():
                    st.write('Place in the paper recycling bin. ')
            
            elif pred_class == "ce_marking":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    with st.expander('See Explanation'):
                        st.markdown("<h3 style='text-align: center; color: grey;'>CE Mark</h3>", unsafe_allow_html=True)
                        st.divider()
                        st.write('This logo indicates conformity with health, safety, and environmental protection standards for products sold within the European Economic Area. this is not a recycling logo.') 
                        st.write('steps on how to recycle / dispose material please follow local disposal guidelines. ')
                
            elif pred_class == "aluminium":
                with st.container(border=True):
                    col_logo = st.columns(2)
                    with col_logo[0]:
                        st.markdown("<h3 style='text-align: center; color: grey;'>Uploaded Picture</h3>", unsafe_allow_html=True)
                        st.image(cropped_image, use_column_width=False)
                    with col_logo[1]:   
                        st.markdown("<h3 style='text-align: center; color: grey;'>Predicted Logo</h3>", unsafe_allow_html=True)
                with st.container():
                    st.write(pred_class)
                    st.write('This logo indicates that the item is made from aluminum, a highly recyclable material. due to this it is recycable') 
                with st.container():
                    st.write('steps on how to recycle / dispose material is by rinsing out any food residue and place in the recycling bin. ')
            
            else:
                st.write('Logo undetected! Please try again.')
                st.write('List of logos that can be detected:')
                st.write('...') # To make list
        
    