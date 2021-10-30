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

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Product image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, '/Shoes/keras_model.h5')
    if label == 0:
        st.write("Superstar")
    elif label == 1:
        st.write("Football FTW Men")
    elif label == 2:
        st.write("Yeezy")
    elif label == 3:
        st.write("Dr. Martens")
    else:
        st.write("New Balance")


