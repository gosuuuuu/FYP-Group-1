# Import Libraries
import streamlit as st
from PIL import Image, ImageChops
from streamlit_option_menu import option_menu
from logo_identifier import LogoClassfier
from streamlit_cropper import st_cropper
from streamlit_modal import Modal

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
        <div style="text-align:center;">
             <img src="{logo_url}" alt="Logo" style="width:300px;">
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

#################### OPTION MENU #################### to be changed?
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

# Home Page
if menu == 'Home':
    tab1, tab2 = st.tabs(['Description', 'Recycle Logos'])

    with tab1: # Description Tab
        st.title("This is the Description tab. \n")
        st.write("Recycling symbols are used to help us identify different types of packaging and if they are capable of being recycled.  \n"
         "They can be confusing, so we are here to help you make sense of them and hopefully increase what you recycle in and out of the home.")
        

    with tab2: # Recycle Logos Tab
        st.title("This is the Recycle Logos tab \n")
        st.write("Few logos that included in the project")

        col1, col2, col3, col4 = st.columns([3,6,3,6])

        with col1:
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/aluminium.png" 
                        alt="Aluminium Logo" 
                        width="200">
                    <p>Aluminium Logo</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.subheader("Aluminium")
            st.markdown(
            """
            <p style='font-size:100px;'>
            The Recyclable Aluminium Recyclable Aluminium Indicates that the item is made from aluminum, a highly recyclable material.
            </p>
            """,
            unsafe_allow_html=True,
            )

        with col3:
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/ce.png" 
                        alt="Aluminium Logo" 
                        width="250">
                    <p>Aluminium Logo</p>
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
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/fsc.png" 
                        alt="Aluminium Logo" 
                        width="200">
                    <p>Aluminium Logo</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col6:
            st.subheader("FSC")
            st.write(
                """
                This certifies that the wood or paper products come from responsibly managed forests.  
                """
            )
            
        with col7:
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/mobiusloop.png" 
                        alt="Aluminium Logo" 
                        width="200">
                    <p>Aluminium Logo</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col8:
            st.subheader("Mobius Loop")
            st.write(
                """
                This represents that the product is recyclable.  
                """
            )

        col9, col10, col11, col12 = st.columns([3,6,3,6])

        with col9:
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png" 
                        alt="Aluminium Logo" 
                        width="200">
                    <p>Aluminium Logo</p>
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
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png" 
                        alt="Aluminium Logo" 
                        width="200">
                    <p>Aluminium Logo</p>
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
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/tidyman.png" 
                        alt="Aluminium Logo" 
                        width="200">
                    <p>Aluminium Logo</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col14:
            st.subheader("Tidyman")
            st.write(
                """
                A symbol encouraging proper waste disposal.  
                """
            )

        with col15:
            st.markdown(
                """
                <div style='text-align: center;'>
                    <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/waste.png" 
                        alt="Aluminium Logo" 
                        width="200">
                    <p>Aluminium Logo</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col16:
            st.subheader("Electric Waste and Battery")
            st.write(
                """
                he crossed-out wheelie bin symbol on your electrical product, batteries, or their packaging, reminds you that all electrical and electronic products and batteries must be recycled through either a recycling centre or with retailers. 
                """
            )

    # with tab3: # Contact tab

    #     st.title(":envelope: Get In Touch With Us!")

    #     contact_form = """
    #         <style>
    #         form {
    #             width: 100%;
    #         }
    #         input[type=text], input[type=email], textarea {
    #             width: 100%;
    #             padding: 12px;
    #             border: 1px solid #ccc;
    #             border-radius: 4px;
    #             box-sizing: border-box;
    #             margin-top: 6px;
    #             margin-bottom: 16px;
    #             background-color: #FFFFFF;
    #         }
    #         textarea {
    #             resize: vertical;
    #         }
    #         button[type=submit] {
    #             background-color: #04AA6D;
    #             color: white;
    #             padding: 12px 20px;
    #             border: none;
    #             border-radius: 4px;
    #             cursor: pointer;
    #         }
    #         button[type=submit]:hover {
    #             background-color: #45a049;
    #         }
    #         </style>
    #         <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
    #             <input type="hidden" name="_captcha" value="false">
    #             <input type="text" name="name" placeholder="Your name" required>
    #             <input type="email" name="email" placeholder="Your email" required>
    #             <textarea name="message" placeholder="Your message here"></textarea>
    #             <button type="submit">Send</button>
    #         </form>
    #     """
    #     st.markdown(contact_form, unsafe_allow_html=True)

# insert description of website
# how to use upload function steps
# table of contents with links

# Upload Page
if menu == 'Upload Logo Prediction':
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
                        pred_class = my_prediction.model_upload(cropped_image, loaded_img)        
    
    else:
        st.write('Please upload an image.')