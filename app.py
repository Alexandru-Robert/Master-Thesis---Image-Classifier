from PIL import Image
from keras.models import load_model
import streamlit as st
from PIL import Image, ImageOps
from img_classification import teachable_machine_classification
from explore_page import show_explore_page
import numpy as np
import cloudinary
import cloudinary.uploader
import cloudinary.api

st.set_page_config(page_title="MasterThesis", page_icon=None,layout='centered', initial_sidebar_state='auto')
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

#need to see how to do if single product image is uploaded. Now it classifies for all classes

add_selectbox = st.sidebar.selectbox(
    "What type of pictures are there going to be added? Single product or multiple product?",
    ("Single Product", "Multiple product")
)

CLOUDINARY_URL=cloudinary://461531742435772:shF0nm0r22IFe3wFXAKynxIr82s@stibodata
cloudinary.config( 
  cloud_name = "stibodata", 
  api_key = "461531742435772", 
  api_secret = "shF0nm0r22IFe3wFXAKynxIr82s",
  secure = true
)

def shoes_accuracy():
    shoes_model = load_model('Shoes_keras_model.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(uploaded_file)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    prediction = shoes_model.predict(data)
    st.write(prediction)


def pants_accuracy():
    shoes_model = load_model('keras_modelPantsv2.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(uploaded_file)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    prediction = shoes_model.predict(data)
    st.write(prediction)


def shirts_accuracy():
    shoes_model = load_model('Shirts_keras_model.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(uploaded_file)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    prediction = shoes_model.predict(data)
    st.write(prediction)


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Product image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    #shoes_accuracy()
    label = teachable_machine_classification(image, 'Shoes_keras_model.h5')
    #st.write(label)
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

    #pants_accuracy()
    label = teachable_machine_classification(image, 'keras_modelPantsv2.h5')
    #st.write(label)
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

    #shirts_accuracy()
    label = teachable_machine_classification(image, 'Shirts_keras_model.h5')
    #st.write(label)
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

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Shoes")
        options = st.multiselect(
        'What shoe model is in the picture?',
        ['RunFalcon 2.0', 'Supernova', 'Ultraboost 5.0 DNA', 'Ultraboost 21','X9000 L3','ZG21','Adicross Retro','Adic XZ Prime Blue', 'Terrex Swift', 'Terrex Voyajer 21 Travel', 'Terrex Free Hiker Prime Blue'])
        #st.write('You selected:', options)
    with col2:
        st.header("Pants/Shorts")
        options = st.multiselect(
        'What Pants/Shorts model is in the picture?',
        ['4KRFT', 'Aerostripes 3 slim', 'FiveTen FeelsBlock','Terrex Hike', 'LiteFlex Hiking', 'ZupaHike Hiking', 'Ultimate 365 Tapered','Ultimate 365 Core Shorts'])
    with col3:
        st.header("Shirts")
        options = st.multiselect(
        'What Shirt model is in the picture?',
        ['SportsWear Logo', 'EssentialsEmbroidedLinearLogo', 'OwnTheRun', 'Runner','BSC 3StripesInsulatedJacket', 'MyShelter RegnJakke', 'Terrex Multi Prime Green Full Zip Fleece Jakke', 'Adicross Evolution', 'GoToPolo', 'GoToPrimeGreenPique', 'Performance PrimeGreen'])

def upload(file, **options)

if st.button('SUBMIT'):
    st.write('The image is being uploaded to the cloud wth the corrected classification')
    cloudinary.uploader.upload(image)
else:
    #st.write('Goodbye')