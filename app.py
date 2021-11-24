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
from io import BytesIO, StringIO
from random import random
import random

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

st.title("Automatic Image Classifier")
st.header("Product image classification")
st.text("Upload a product Image for image classification as different classes")

uploaded_file = st.file_uploader("Choose a product image ...")#, type="jpeg")

# uploaded_files = st.file_uploader("Choose a product image", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#      bytes_data = uploaded_file.read()
#      st.write("filename:", uploaded_file.name)
#      st.write(bytes_data)

CLOUDINARY_URL = 'cloudinary://461531742435772:shF0nm0r22IFe3wFXAKynxIr82s@stibodata'

cloudinary.config( 
  cloud_name = "stibodata", 
  api_key = "461531742435772", 
  api_secret = "shF0nm0r22IFe3wFXAKynxIr82s",
  #secure = true
)

running = ['RunFalcon 2.0', 'Supernova', 'Ultraboost 5.0 DNA', 'Ultraboost 21','X9000 L3','4KRFT', 'Aerostripes 3 slim','SportsWear Logo', 'EssentialsEmbroidedLinearLogo', 'OwnTheRun', 'Runner']
outdoor = ['Terrex Swift', 'Terrex Voyajer 21 Travel', 'Terrex Free Hiker Prime Blue','FiveTen FeelsBlock','Terrex Hike', 'LiteFlex Hiking', 'ZupaHike Hiking','BSC 3StripesInsulatedJacket', 'MyShelter RegnJakke', 'Terrex Multi Prime Green Full Zip Fleece Jakke']
golf = ['ZG21','Adicross Retro','Adic XZ Prime Blue','Ultimate 365 Tapered','Ultimate 365 Core Shorts','Adicross Evolution', 'GoToPolo', 'GoToPrimeGreenPique', 'Performance PrimeGreen']

imageTags = []
imageTitle = []
imageDescription = ''

def shoes_accuracy():
    shoes_model = load_model('Shoes_keras_model.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    #data.round(2)
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
    #labelshoes = normalized_image_array
    prediction = shoes_model.predict(data)*100
    confidence = np.amax(prediction) 
    st.write(confidence,"%")
    # st.dataframe(prediction.round(2))
    #st.write(prediction)

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
    prediction = shoes_model.predict(data)*100
    confidence = np.amax(prediction) 
    st.write(confidence,"%")
    #st.write(prediction)

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
    prediction = shoes_model.predict(data)*100
    confidence = np.amax(prediction) 
    st.write(confidence,"%")
    #st.write(prediction)

#need to see how to do if single product image is uploaded. Now it classifies for all classes
smsb = st.sidebar.selectbox("What type of pictures are there going to be added? Single product or multiple product?",("Multiple product","Single Product"))

#LABELS
output_label_shoes = ['RunFalcon 2.0', 'Supernova', 'Ultraboost 5.0 DNA', 'Ultraboost 21','X9000 L3','ZG21','Adicross Retro','Adic XZ Prime Blue', 'Terrex Swift', 'Terrex Voyajer 21 Travel', 'Terrex Free Hiker Prime Blue']
output_label_pants = ['4KRFT', 'Aerostripes 3 slim', 'FiveTen FeelsBlock','Terrex Hike', 'LiteFlex Hiking', 'ZupaHike Hiking', 'Ultimate 365 Tapered','Ultimate 365 Core Shorts']
output_label_shirts = ['SportsWear Logo', 'EssentialsEmbroidedLinearLogo', 'OwnTheRun', 'Runner','BSC 3StripesInsulatedJacket', 'MyShelter RegnJakke', 'Terrex Multi Prime Green Full Zip Fleece Jakke', 'Adicross Evolution', 'GoToPolo', 'GoToPrimeGreenPique', 'Performance PrimeGreen']


checker_for_no_img = 0
def shirts_user_input(x):
    global imageTags
    global imageTitle
    global imageDescription
    with st.container():
        col1, col2, col3 = st.columns(3)
        with x:
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                label = teachable_machine_classification(image, 'Shirts_keras_model.h5')
                st.header("Shirts")
                checker_for_no_img = 1
                labelint = label.item()
                optionSingleShirts = st.selectbox(
                        'Shirt model in the picture.',
                        ['Unknown','SportsWear Logo', 'EssentialsEmbroidedLinearLogo', 'OwnTheRun', 'Runner','BSC 3StripesInsulatedJacket', 'MyShelter RegnJakke', 'Terrex Multi Prime Green Full Zip Fleece Jakke', 'Adicross Evolution', 'GoToPolo', 'GoToPrimeGreenPique', 'Performance PrimeGreen'],
                        index= labelint +1
                        )
                if optionSingleShirts in running:
                    imageTags += 'Running' #+ optionSingleShirs
                    imageTitle += optionSingleShirts
                elif optionSingleShirts in outdoor:
                    imageTitle += optionSingleShirts
                    imageTags += 'Outdoor' #+ optionSingleShoes
                elif optionSingleShirts in golf:
                    imageTitle += optionSingleShirts
                    imageTags += 'Golf' #+ optionSingleShoes
                else:
                    imageTags +=  'Unknown'
                    imageTitle += 'Unknown'
                    imageDescription ='Must be Classified, class not found' 
                    st.write('The selected shirt class is not available')
                #st.write(imageTitle)
                #st.write(imageTags)
            #else:
            #    st.header("Add an Image")
            #st.write('You selected:', options)
            # st.write(optionSingleShoes)

def shoes_user_input(y):
    global imageTags
    global imageTitle
    global imageDescription
    with st.container():
        col1, col2, col3 = st.columns(3)
        with y:
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                label = teachable_machine_classification(image, 'Shoes_keras_model.h5')
                labelint = label.item()
                checker_for_no_img = 1
                st.header("Shoes")
                optionSingleShoes = st.selectbox(
                'Shoes model in the picture.',
                ['Unknown','RunFalcon 2.0', 'Supernova', 'Ultraboost 5.0 DNA', 'Ultraboost 21','X9000 L3','ZG21','Adicross Retro','Adic XZ Prime Blue', 'Terrex Swift', 'Terrex Voyajer 21 Travel', 'Terrex Free Hiker Prime Blue'],
                index = labelint + 1)                    
                if optionSingleShoes in running:
                    imageTags += 'Running' #+ optionSingleShoes
                    imageTitle += optionSingleShoes
                elif optionSingleShoes in outdoor:
                    imageTitle += optionSingleShoes
                    imageTags += 'Outdoor' #+ optionSingleShoes
                elif optionSingleShoes in golf:
                    imageTitle += optionSingleShoes
                    imageTags += 'Golf' #+ optionSingleShoes
                else:
                    imageTags +=  'Unknown'
                    imageTitle += 'Unknown'
                    imageDescription += 'Must be Classified, class not found' 
                    st.write('The selected shoe class is not available')
                #st.write(imageTags)
                #st.write(imageTitle)
            #else:
            #    st.header("Add an Image")
                #st.write('You selected:', options)
                # st.write(optionSingleShoes)

def pants_user_input(z):
    global imageTags
    global imageTitle
    global imageDescription    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with z:
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                label = teachable_machine_classification(image, 'Pants_keras_model.h5')
                labelint = label.item()
                checker_for_no_img = 1
                st.header("Pants/Shorts")
                optionSinglePants = st.selectbox(
                    'Pants/Shorts model in the picture.',
                    ['Unknown','4KRFT', 'Aerostripes 3 slim', 'FiveTen FeelsBlock','Terrex Hike', 'LiteFlex Hiking', 'ZupaHike Hiking', 'Ultimate 365 Tapered','Ultimate 365 Core Shorts'],
                    index= labelint + 1)
                if optionSinglePants in running:
                    imageTags += 'Running' #+ optionSinglePants
                    imageTitle += optionSinglePants
                elif optionSinglePants in outdoor:
                    imageTitle += optionSinglePants
                    imageTags += 'Outdoor' #+ optionSingleShoes
                elif optionSinglePants in golf:
                    imageTitle += optionSinglePants
                    imageTags += 'Golf' #+ optionSingleShoes
                else:
                    imageTags +=  'Unknown'
                    imageTitle += 'Unknown'
                    imageDescription += 'Must be Classified, class not found' 
                    st.write('The selected pants class is not available')
                #st.write(imageTags)
                #st.write(imageTitle)
            #else:
             #   st.header("Add an Image")
            #st.write('You selected:', options)
            # st.write(optionSingleShoes)


if smsb == "Single Product":
    csb= st.sidebar.selectbox("What category does the product belong to?",("Shoes", "Pants/Shorts", "Shirts"))
    if csb == "Shoes":
        if uploaded_file is not None:
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col2:
                    image = Image.open(uploaded_file)
                    st.image(image, width=200 ,caption='Uploaded Product image.')            
            st.write("")
            st.write("Classifying...")
            #SHOES
            with st.container():
                col1, col2, col3 = st.columns(3)
                #OUTPUT LABEL OF SHOES
                with col1:
                    label = teachable_machine_classification(image, 'Shoes_keras_model.h5')
                    st.write(output_label_shoes[label])
                #CONFIDENCE LEVEL OF SHOES
                with col2:
                    shoes_accuracy()            
        #User Input
        with st.container():
            col1, col2, col3 = st.columns(3)
            shoes_user_input(col1)
    elif csb == "Pants/Shorts":
        if uploaded_file is not None:
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col2:
                    image = Image.open(uploaded_file)
                    st.image(image, width=200 ,caption='Uploaded Product image.')            
            st.write("")
            st.write("Classifying...")      
            #PANTS
            with st.container():
                col1, col2, col3 = st.columns(3)
                #OUTPUT LABEL OF PANTS    
                with col1:
                    label = teachable_machine_classification(image, 'keras_modelPantsv2.h5')
                    st.write(output_label_pants[label])
                #CONFIDENCE LEVEL OF PANTS    
                with col2:
                    pants_accuracy()  
        #User Input
        with st.container():
            col1, col2, col3 = st.columns(3)
            pants_user_input(col1)
    else:
        if uploaded_file is not None:
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col2:
                    image = Image.open(uploaded_file)
                    st.image(image, width=200 ,caption='Uploaded Product image.')            
            st.write("")
            st.write("Classifying...")
            #SHIRTS
            with st.container():
                col1, col2, col3 = st.columns(3)
                #OUTPUT LABEL OF SHIRTS
                with col1:
                    label = teachable_machine_classification(image, 'Shirts_keras_model.h5')
                    st.write(output_label_shirts[label])
                #CONFIDENCE LEVEL OF SHIRTS
                with col2:
                    shirts_accuracy()
        #User Input
        with st.container():
            col1, col2, col3 = st.columns(3)
            shoes_user_input(col1)
else:
    if uploaded_file is not None:
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col2:
                image = Image.open(uploaded_file)
                st.image(image, width=200 ,caption='Uploaded Product image.')            
        st.write("")
        st.write("Classifying...")
        #SHOES LABEL & ACC
        with st.container():
            col1, col2, col3 = st.columns(3)
            #OUTPUT LABEL OF SHOES
            with col1:
                label = teachable_machine_classification(image, 'Shoes_keras_model.h5')
                st.write(output_label_shoes[label])
            #CONFIDENCE LEVEL OF SHOES
            with col2:
                shoes_accuracy()    
        #PANTS LABEL & ACC
        with st.container():
            col1, col2, col3 = st.columns(3)
            #OUTPUT LABEL OF PANTS    
            with col1:
                label = teachable_machine_classification(image, 'keras_modelPantsv2.h5')
                st.write(output_label_pants[label])
            #CONFIDENCE LEVEL OF PANTS    
            with col2:
                pants_accuracy()
        #SHIRTS LABEL & ACC
        with st.container():
            col1, col2, col3 = st.columns(3)
            #OUTPUT LABEL OF SHIRTS
            with col1:
                label = teachable_machine_classification(image, 'Shirts_keras_model.h5')
                st.write(output_label_shirts[label])
            #CONFIDENCE LEVEL OF SHIRTS
            with col2:
                shirts_accuracy()

    #User Input
    with st.container():
        col1,col2,col3 = st.columns(3)
        shirts_user_input(col1)
        shoes_user_input(col2)
        pants_user_input(col3)


# def upload(file, **options):
#     st.write('')


randomID = random.randint(0, 999999)
#st.write(randomID)

if st.button('SUBMIT'):
    st.write('The image is being uploaded to the cloud wth the corrected classification')
    with BytesIO() as buf:
        image.save(buf, 'jpeg')
        image_bytes = buf.getvalue()
    cloudinary.uploader.upload(image_bytes, 
    folder = "SampleImages/" + imageTags +"/", 
    tags = imageTags,
    public_id = imageTitle+str(randomID),
    caption = str(imageTitle)
    #overwrite = true, 
    #notification_url = "https://mysite.example.com/notify_endpoint", 
    #resource_type = "image"
    )