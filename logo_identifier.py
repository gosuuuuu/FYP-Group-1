# Import Libraries
import numpy as np
import tensorflow as tf
import streamlit as st


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

        cropped_image = cropped_image.resize((224,224))  
        
        if pred_class == "tidyman":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style="display: flex; justify-content: center;">
                            <img src="data:image/png;base64,{cropped_image}" style="width: 224px; height: 224px;">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    #st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <<div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/tidyman.png" 
                                width="180">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Tidyman</h2>", unsafe_allow_html=True)
                st.write('This symbol defines as a reminder towards consumers for proper waste disposal.')
            with st.container():
                st.write('This symbol is a reminder to dispose waste responsibly. It encourages consumers to throw their trash into appropriate trash cans to help keep the environment clean. Although it not a recycling logo, it promotes good waste management practices.')
                
        elif pred_class == "plastic_PS":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Plastic Logo 6 - PS</h2>", unsafe_allow_html=True)
                st.write('This plastic product is often used for disposable cutlery and foam containers. It is not easily recyclable.') 
            with st.container():
                st.write('This plastic material is typically not accepted in curbside recycling and needs to go to specialized centers such as Sallima Recycling Works in Berakas, Brunei Darussalam. Proper disposal helps prevent harm towards the environment, as polystyrene is not biodegradable. Visit Sallima Recycling Works for more details.')
                st.link_button("Visit Sallima Recycling Works", "https://boxlocator.eu/en/detail/box//uid/6137035685-27", 
                               use_container_width=True)

        elif pred_class == "plastic_PP":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Plastic Logo 5 - PP</h2>", unsafe_allow_html=True)
                st.write('This plastic logo is a recycable plastic material, usually used for containers, straws, and several packaging products.') 
            with st.container():
                st.write('This material can be recycled but encouraged to send to specialized facilities for recycling this material. Proper recycling ensures that this durable plastic does not end up in landfills as it may cause harm. Check local centers like EnEvo Sdn Bhd for acceptance. More information is available at EnEvo Brunei. ')
                st.link_button("Visit EnEvo Sdn Bhd", "https://enevobrunei.com",
                               use_container_width=True)
        
        elif pred_class == "plastic_PET":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Plastic Logo 1 - PET</h2>", unsafe_allow_html=True)
                st.write('This plastic logo is a recycable plastic used for containers, straws, and several packagings.') 
            with st.container():
                st.write('This plastic material is commonly recycled and can usually be dropped off at The Green Depot. Recycling PET products helps reduce plastic pollution and conserve resources. Check out The Green Depot for more details.')
                st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn",
                               use_container_width=True)

        elif pred_class == "plastic_PAP":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Plastic Logo 20, 21, 22 - PAP</h2>", unsafe_allow_html=True)
                st.write('This plastic logo contains a plastic material that usually are sent to local facilities as it is recycable. It is used in various applications, including textiles and packagings. ') 
            with st.container():
                st.write('This material is easily recyclable and typically accepted at The Green Depot in Brunei. Recycling paper reduces deforestation and energy consumption. Visit The Green Depot for more information.')
                st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn",
                               use_container_width=True)
        
        elif pred_class == "plastic_other":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Plastic Logo 7 - Other</h2>", unsafe_allow_html=True)
                st.write('This plastic logo is recyclable but depends on the specific type; check local guidelines it is recycable. This logo covers various types of plastic that do not fit into the other categories.') 
            with st.container():
                st.write('This logo refers to various plastics that are often not easily recyclable and may need to be processed at specific recycling centers such as Kawan Bumi Sdn. Bhd. in Mulaut. For responsible disposal of such plastics, contact Kawan Bumi.')
                st.link_button("Visit Kawan Bumi Sdn. Bhd", "https://www.kawanbumi.com",
                               use_container_width=True)
        
        elif pred_class == "plastic_LDPE":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Plastic Logo 4 - LDPE</h2>", unsafe_allow_html=True)
                st.write('It is often used for plastic bags and some containers. It is recycable, but only at specific facilities.') 
            with st.container():
                st.write('LDPE generally not accepted in curbside recycling. It must be taken to specialized centers like Daikyorecycling in Muara. Using such centers ensures the plastic is processed in an environmentally friendly way. Visit Daikyorecycling for details. ')
                st.link_button("Visit Daikyorecycling", "http://www.daikyorecycle.com",
                               use_container_width=True)
        
        elif pred_class == "plastic_HDPE":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/plastic.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Plastic Logo 2 - HDPE</h2>", unsafe_allow_html=True)
                st.write('This plastic logo is commonly used for containers like milk jugs and detergent bottles. It is recycable ') 
            with st.container():
                st.write('This plastic is widely recyclable and can be processed at The Green Depot in Brunei. Recycling HDPE helps reduce plastic waste in the environment. More information is available at The Green Depot.')
                st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn",
                               use_container_width=True)
        
        elif pred_class == "period_36m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Period of Opening - 36 Months</h2>", unsafe_allow_html=True)
                st.write('This logo indicates the product should be used within 36 months after opening. Depending on the material, it is recycable') 
            with st.container():
                st.write("This symbol refers to the recommended duration for safe use of a product after it has been opened. It ensures product freshness and safety for consumers. It’s best to dispose of these products after the indicated time frame to ensure they remain safe to use, but note that these symbols are not related to recyclability.")
        
        elif pred_class == "period_24m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Period of Opening - 24 Months</h2>", unsafe_allow_html=True)
                st.write('This logo Indicates the product should be used within 24 months after opening. Depending on the material it is recycable') 
            with st.container():
                st.write("This symbol refers to the recommended duration for safe use of a product after it has been opened. It ensures product freshness and safety for consumers. It’s best to dispose of these products after the indicated time frame to ensure they remain safe to use, but note that these symbols are not related to recyclability.")
        
        elif pred_class == "period_12m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Period of Opening - 12 Months</h2>", unsafe_allow_html=True)
                st.write('This logo indicates the product should be used within 12 months after opening. Depending on the material, it is recycable') 
            with st.container():
                st.write("This symbol refers to the recommended duration for safe use of a product after it has been opened. It ensures product freshness and safety for consumers. It’s best to dispose of these products after the indicated time frame to ensure they remain safe to use, but note that these symbols are not related to recyclability.")
        
        elif pred_class == "period_9m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Period of Opening - 9 Months</h2>", unsafe_allow_html=True)
                st.write('This logo indicates the product should be used within nine months after opening. Depending on the material, it is recycable') 
            with st.container():
                st.write("This symbol refers to the recommended duration for safe use of a product after it has been opened. It ensures product freshness and safety for consumers. It’s best to dispose of these products after the indicated time frame to ensure they remain safe to use, but note that these symbols are not related to recyclability.")
        
        elif pred_class == "period_6m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Period of Opening - 6 Months</h2>", unsafe_allow_html=True)
                st.write('This logo indicates the product should be used within six months after opening. Depending on the material, it is recycable') 
            with st.container():
                st.write("This symbol refers to the recommended duration for safe use of a product after it has been opened. It ensures product freshness and safety for consumers. Its best to dispose of these products after the indicated time frame to ensure they remain safe to use, but note that these symbols are not related to recyclability.")
        
        elif pred_class == "period_3m":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/pao.png"  
                                width="200">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Period of Opening - 3 Months</h2>", unsafe_allow_html=True)
                st.write('This logo indicates the product should be used within three months after opening. Depending on the material, it is recycable') 
            with st.container():
                st.write("This symbol refers to the recommended duration for safe use of a product after it has been opened. It ensures product freshness and safety for consumers. It is best to dispose of these products after the indicated time frame to ensure they remain safe to use, but note that these symbols are not related to recyclability.")
        
        elif pred_class == "mobius_logo":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                    """
                    <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                        <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/mobiusloop.png" 
                            width="180">
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Mobius Logo</h2>", unsafe_allow_html=True)
                st.write('This logo represents that the product is recyclable.') 
            with st.container():
                st.write('This symbol indicates recyclability, though whether a product can be recycled easily depends on local facilities. In Brunei, it may require specialized facilities like The Green Depot. Visit The Green Depot for more information.')
                st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn",
                               use_container_width=True)

        elif pred_class == "fsc":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/fsc.png" 
                                width="170">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Forest Stewardship Council (FSC)</h2>", unsafe_allow_html=True)
                st.write('This logo certifies that the wood or paper products come from responsibly managed forests. It is recycable.') 
            with st.container():
                st.write('This symbol stands for Forest Stewardship Council, indicating sustainable sourcing of wood products. It ensures that the materials come from responsibly managed forests, promoting environmental sustainability. FSC-certified products can also be recycled at The Green Depot. More details can be found at The Green Depot.')
                st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn",
                               use_container_width=True)
        
        elif pred_class == "ce_marking":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                    """
                    <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                        <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/ce.png"  
                            width="230">
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>CE Mark</h2>", unsafe_allow_html=True)
                st.write('Although this is not a recycling logo, it is an indication of conformity with health, safety, and environmental protection standards for products sold within the European Economic Area.') 
            with st.container():
                st.write('While it is not a recycling logo and does not imply recyclability, products with this mark meet stringent environmental and safety requirements.')
            
        elif pred_class == "aluminium":
            with st.container(border=True):
                col_logo = st.columns(2)
                with col_logo[0]:
                    st.markdown("<h2 style='text-align: center; color: grey;'>Uploaded Picture</h2>", unsafe_allow_html=True)
                    st.image(cropped_image, use_column_width=False)
                with col_logo[1]:   
                    st.markdown("<h2 style='text-align: center; color: grey;'>Predicted Logo</h2>", unsafe_allow_html=True)
                    st.markdown(
                        """
                        <div style='text-align: center; margin: 0px 0px 100px 0px;'>
                            <img src="https://raw.githubusercontent.com/gosuuuuu/FYP-Group-1/main/Recycle%20Logo/aluminium.png" 
                                alt="Aluminium Logo" 
                                width="180">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            with st.container():
                st.markdown("<h2 style='text-align: center; color: grey;'>Aluminium</h2>", unsafe_allow_html=True)
                st.write('This logo indicates that the item is made from aluminum, a highly recyclable material.') 
            with st.container():
                st.write('This logo represents aluminum, which can be recycled at The Green Depot in Kuala Belait but typically requires specialized processing. Recycling aluminum helps reduce energy consumption and environmental impact. For more information, visit The Green Depot.')
                st.link_button("Visit The Green Depot", "https://www.instagram.com/greendepotbn",
                               use_container_width=True)
        
        else:
            st.write('Logo undetected! Please try again.')
            st.write('List of logos that can be detected:')
            st.write('...') # To make list
        
    