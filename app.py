from PIL import Image
import streamlit as st
from PIL import Image, ImageOps
from img_classification import teachable_machine_classification
from explore_page import show_explore_page

st.set_page_config(page_title="MasterThesis", page_icon=None, layout='centered', initial_sidebar_state='auto')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

hide_st_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

hide_footer_style = """
            <style>
            .reportview-container .main footer {visibility: hidden;}    
            """
st.markdown(hide_footer_style, unsafe_allow_html=True)

# page = st.sidebar.selectbox("Data Explore Or Home", ("Home", "Explore"))
# if page == "Explore":
#     show_explore_page()

st.title("Image Classification ")
st.header("Product image classification")
st.text("Upload a product Image for image classification as different classes")

uploaded_file = st.file_uploader("Choose a product image ...")#, type="jpeg")

# uploaded_files = st.file_uploader("Choose a product image", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#      bytes_data = uploaded_file.read()
#      st.write("filename:", uploaded_file.name)
#      st.write(bytes_data)

def

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Product image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")


    label = teachable_machine_classification(image, 'Shoes_keras_model.h5')
    st.write(label)
    if label == 0:
        st.write("RunFalcon 2.0")
    elif label == 1:
        st.write("Supernova")
    elif label == 2:
        st.write("Ultraboozt 5.0 DNA")
    elif label == 3:
        st.write("Ultraboost 21")
    elif label == 4:
        st.write("X9000 L3")
    elif label == 5:
        st.write("ZG21")
    elif label == 6:
        st.write("Adicross Retro")
    elif label == 7:
        st.write("Adic XZ Prime Blue")
    elif label == 8:
        st.write("Terrex Swift")
    elif label == 9:
        st.write("Terrex Voyajer 21 Travel")
    else:
        st.write("Terrex Free Hiker Prime Blue")

    label = teachable_machine_classification(image, 'Pants_keras_model.h5')
    st.write(label)
    if label == 0:
        st.write("4KRFT")
    elif label == 1:
        st.write("Aerostripes 3 slim")
    elif label == 2:
        st.write("FiveTenFeelsBlockBusker")
    elif label == 3:
        st.write("TerrexHikeBusker")
    elif label == 4:
        st.write("LiteflexHikingBusker")
    elif label == 5:
        st.write("ZupahikeHikingBusker")
    elif label == 6:
        st.write("Ultimate 365 Tapered Bukser")
    else:
        st.write("Utimate365 Core Shorts")

    label = teachable_machine_classification(image, 'Shirts_keras_model.h5')
    st.write(label)
    if label == 0:
        st.write("SportsWearLogo")
    elif label == 1:
        st.write("EssentialsEmbroidedLinearLogo")
    elif label == 2:
        st.write("OwnTheRun")
    elif label == 3:
        st.write("Runner")
    elif label == 4:
        st.write("BSC 3Stripes Insulated Jacket")
    elif label == 5:
        st.write("MyShelter RegnJakke")
    elif label == 6:
        st.write("Terrex Multi Prime Green Full Zip Fleece Jakke")
    elif label == 7:
        st.write("Adicross Evolution")
    elif label == 8:
        st.write("GoToPolo")
    elif label == 9:
        st.write("GoToPrimeGreenPique")
    else:
        st.write("PerformancePrimeGreen")
