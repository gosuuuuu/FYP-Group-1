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


def black_font():
    st.markdown(
        """ <style>
        * {color: black !important;
            font-size: 23px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

black_font()

# To be changed
#st.markdown("<h1 style='text-align: center; color: black; background-color: #b8ffbc'>I D E N T I L O G</h1>", 
            #unsafe_allow_html=True)

#################### LOGO ####################

# Using URL #
import streamlit as st

def set_logo(logo_url):
    st.markdown(
        f"""
        <div style="text-align:center;">
             <img src="{logo_url}" alt="Logo" style="width:300px;">
        </div>
        """,
        unsafe_allow_html=True
    )

logo_url = "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Logo%20and%20Background/BlackFontBG.png"
set_logo(logo_url)

# Using Local #

# def set_logo(logo_path):
    
#     with open(logo_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
    
#     st.markdown(
#         f"""
#         <div style="text-align:center;">
#              <img src="data:image/png;base64,{encoded_string}" alt="Logo" style="width:300px;">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# logo_path = r"C:\Users\insya\Desktop\Black_BG.png"
# set_logo(logo_path)

#################### BACKGROUND IMAGE ####################

# Using URL #

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


# Using Lokal #

# def set_bg(img_path):
#     bg_ext = 'png'
    
#     with open(img_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
    
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background: url(data:image/{bg_ext};base64,{encoded_string})
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# img_bg = r"C:\Users\insya\Pictures\Wallpaper\Lock Screen.jpg"
# set_bg(img_bg)

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
        st.title("This is the Description tab. \n")
        st.write("Recycling symbols are used to help us identify different types of packaging and if they are capable of being recycled.  \n"
         "They can be confusing, so we are here to help you make sense of them and hopefully increase what you recycle in and out of the home.")
        

    with tab2:
        st.title("This is the Recycle Logos tab \n")
        st.write("Few logos that included in the project")

        st.markdown(
            """
            <style>
            .col-container {
                display: flex;
                align-items: center;
            }
            .col-container .col {
                margin-right: 1000px;  /* Adjust this value to increase or decrease spacing between columns */
            }
            .col-container .col:last-child {
                margin-right: 100px;  /* No margin for the last column */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        with st.container():
            st.markdown('<div class="col-container">', unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns([1,2,3,4])

            with col1:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/aluminium.png",
                    caption="Aluminium Logo",
                    use_column_width=False,
                    width=200,           
                )

            with col2:
                st.subheader("Aluminium")
                st.write(
                    """
                    The Recyclable Aluminium Recyclable Aluminium Indicates that the item is made from aluminum, a highly recyclable material.  
                    """
                )

            with col3:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/ce.png",
                    caption="CE logo",
                    use_column_width=False,
                    width=250,  
                )

            with col4:
                st.subheader("CE")
                st.write(
                    """
                    This indicates conformity with health, safety, and environmental protection standards for products sold within the European Economic Area.  
                    """
                )
            
            st.markdown('</div>', unsafe_allow_html=True)

            col5, col6, col7, col8 = st.columns(4)

            with col5:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/fsc.png",
                    caption="FSC Logo",
                    use_column_width=False,
                    width=200,  
                )

            with col6:
                st.subheader("FSC")
                st.write(
                    """
                    This certifies that the wood or paper products come from responsibly managed forests.  
                    """
                )
            
            with col7:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/mobiusloop.png",
                    caption="Mobius Loop Logo",
                    use_column_width=False,
                    width=200,  
                )

            with col8:
                st.subheader("Mobius Loop")
                st.write(
                    """
                    This represents that the product is recyclable.  
                    """
                )

            col9, col10, col11, col12 = st.columns(4)

            with col9:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png",
                    caption="Period After Opening Logo",
                    use_column_width=False,
                    width=200,  
                )

            with col10:
                st.subheader("Period After Opening")
                st.write(
                    """
                    The period-after-opening (PAO) symbol highlights the amount of time a cosmetic product will remain safe for use after being opened for the first time. It depicts an open cosmetics pot and is used together with a written number of months or years.  
                    """
                )

            with col11:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png",
                    caption="Plastic Logo",
                    use_column_width=False,
                    width=200,  
                )

            with col12:
                st.subheader("Plastic")
                st.write(
                    """
                    These symbols help consumers to identify different types of plastic resin used to make the product.They were applied to help assist with the sorting of plastics. Like many materials plastics should be recycled separately, so the value of the of the recycled material is preserved. Allowing it to be reused to make new products.  
                    """
                )

            col13, col14, col15, col16 = st.columns(4)

            with col13:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/tidyman.png",
                    caption="Tidyman Logo",
                    use_column_width=False,
                    width=200,  
                )

            with col14:
                st.subheader("Tidyman")
                st.write(
                    """
                    A symbol encouraging proper waste disposal.  
                    """
                )

            with col15:
                st.image(
                    "https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/waste.png",
                    caption="Electric Waste and Battery Logo",
                    use_column_width=False,
                    width=200,  
                )

            with col16:
                st.subheader("Electric Waste and Battery")
                st.write(
                    """
                    he crossed-out wheelie bin symbol on your electrical product, batteries, or their packaging, reminds you that all electrical and electronic products and batteries must be recycled through either a recycling centre or with retailers. 
                    """
                )

    with tab3:

        st.title(":envelope: Get In Touch With Us!")

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
                background-color: #FFFFFF;
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
            my_prediction = LogoClassfier('D:\FYP Group 1\my_model.h5')

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
