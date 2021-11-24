from PIL import Image
from keras.models import load_model
import streamlit as st
from PIL import Image, ImageOps
from img_classification import teachable_machine_classification
from explore_page import show_explore_page
import numpy as np
#import cloudinary
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

CLOUDINARY_URL = 'cloudinary://461531742435772:shF0nm0r22IFe3wFXAKynxIr82s@stibodata'

cloudinary.config( 
  cloud_name = "stibodata", 
  api_key = "461531742435772", 
  api_secret = "shF0nm0r22IFe3wFXAKynxIr82s",
  secure = true
)

# cloudinary.uploader.upload("dog.mp4", 
#   folder = "myfolder/mysubfolder/", 
#   public_id = "my_dog",
#   overwrite = true, 
#   notification_url = "https://mysite.example.com/notify_endpoint", 
#   resource_type = "video")

running = ['RunFalcon 2.0', 'Supernova', 'Ultraboost 5.0 DNA', 'Ultraboost 21','X9000 L3','4KRFT', 'Aerostripes 3 slim','SportsWear Logo', 'EssentialsEmbroidedLinearLogo', 'OwnTheRun', 'Runner']
outdoor = ['Terrex Swift', 'Terrex Voyajer 21 Travel', 'Terrex Free Hiker Prime Blue','FiveTen FeelsBlock','Terrex Hike', 'LiteFlex Hiking', 'ZupaHike Hiking','BSC 3StripesInsulatedJacket', 'MyShelter RegnJakke', 'Terrex Multi Prime Green Full Zip Fleece Jakke']
golf = ['ZG21','Adicross Retro','Adic XZ Prime Blue','Ultimate 365 Tapered','Ultimate 365 Core Shorts','Adicross Evolution', 'GoToPolo', 'GoToPrimeGreenPique', 'Performance PrimeGreen']

imageTags = []
imageTitle = ''
imageDescription = ''

def shoes_accuracy():
    shoes_model = load_model('Shoes_keras_model.h5')
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data.round(2)
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
smsb = st.sidebar.selectbox(
    "What type of pictures are there going to be added? Single product or multiple product?",
    ("Multiple product","Single Product")
)

if smsb == "Single Product":
    csb= st.sidebar.selectbox(
    "What category does the product belong to?",
    ("Shoes", "Pants/Shorts", "Shirts"))
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
                #CONFIDENCE LEVEL OF SHOES
                with col2:
                    shoes_accuracy()            
        #User Input
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    label = teachable_machine_classification(image, 'Shoes_keras_model.h5')
                    labelint = label.item()
                    st.header("Shoes")
                    optionSingleShoes = st.selectbox(
                    'What shoes model is in the picture?',
                    ['Unknown','RunFalcon 2.0', 'Supernova', 'Ultraboost 5.0 DNA', 'Ultraboost 21','X9000 L3','ZG21','Adicross Retro','Adic XZ Prime Blue', 'Terrex Swift', 'Terrex Voyajer 21 Travel', 'Terrex Free Hiker Prime Blue'],
                    index = labelint + 1
                    )                    
                    if optionSingleShoes in running:
                        imageTags = optionSingleShoes
                        imageTitle = 'Running'
                    elif optionSingleShoes in outdoor:
                        imageTags = optionSingleShoes
                        imageTitle = 'Outdoor'
                    elif optionSingleShoes in golf:
                        imageTags = optionSingleShoes
                        imageTitle = 'Golf'
                    else:
                        imageTags =  'Unknown'
                        imageTitle = 'Unknown'
                        imageDescription ='Must be Classified, class not found' 
                        st.write('The selected tag is not available')
                    st.write(imageTags)
                    st.write(imageTitle)
                else:
                    st.header("Add an Image")

                #st.write('You selected:', options)
                # st.write(optionSingleShoes)

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
                #CONFIDENCE LEVEL OF PANTS    
                with col2:
                    pants_accuracy()  
        #User Input
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("Pants/Shorts")
                labelint = label.item()
                optionSinglePants = st.selectbox(
                'What Pants/Shorts model is in the picture?',
                ['Unknown','4KRFT', 'Aerostripes 3 slim', 'FiveTen FeelsBlock','Terrex Hike', 'LiteFlex Hiking', 'ZupaHike Hiking', 'Ultimate 365 Tapered','Ultimate 365 Core Shorts'],
                index= labelint + 1
                )
                #if optionSinglePants in 
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
                #CONFIDENCE LEVEL OF SHIRTS
                with col2:
                    shirts_accuracy()
        #User Input
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("Shirts")
                labelint = label.item()
                optionSingleShirts = st.selectbox(
                'What Shirt model is in the picture?',
                ['Unknown','SportsWear Logo', 'EssentialsEmbroidedLinearLogo', 'OwnTheRun', 'Runner','BSC 3StripesInsulatedJacket', 'MyShelter RegnJakke', 'Terrex Multi Prime Green Full Zip Fleece Jakke', 'Adicross Evolution', 'GoToPolo', 'GoToPrimeGreenPique', 'Performance PrimeGreen'],
                index= labelint +1
                )

else:
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
            #CONFIDENCE LEVEL OF SHOES
            with col2:
                shoes_accuracy()    
        #PANTS
        with st.container():
            col1, col2, col3 = st.columns(3)
            #OUTPUT LABEL OF PANTS    
            with col1:
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
            #CONFIDENCE LEVEL OF PANTS    
            with col2:
                pants_accuracy()
        #SHIRTS
        with st.container():
            col1, col2, col3 = st.columns(3)
            #OUTPUT LABEL OF SHIRTS
            with col1:
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
            #CONFIDENCE LEVEL OF SHIRTS
            with col2:
                shirts_accuracy()

    #User Input
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Shoes")
            optionShoes = st.multiselect(
            'Shoes model in the picture:',
            ['RunFalcon 2.0', 'Supernova', 'Ultraboost 5.0 DNA', 'Ultraboost 21','X9000 L3','ZG21','Adicross Retro','Adic XZ Prime Blue', 'Terrex Swift', 'Terrex Voyajer 21 Travel', 'Terrex Free Hiker Prime Blue'])
            #st.write('You selected:', options)
        with col2:
            st.header("Pants/Shorts")
            optionPants = st.multiselect(
            'Pants/Shorts model in the picture:',
            ['4KRFT', 'Aerostripes 3 slim', 'FiveTen FeelsBlock','Terrex Hike', 'LiteFlex Hiking', 'ZupaHike Hiking', 'Ultimate 365 Tapered','Ultimate 365 Core Shorts'])
        with col3:
            st.header("Shirts")
            optionShirts = st.multiselect(
            'Shirt model in the picture:',
            ['SportsWear Logo', 'EssentialsEmbroidedLinearLogo', 'OwnTheRun', 'Runner','BSC 3StripesInsulatedJacket', 'MyShelter RegnJakke', 'Terrex Multi Prime Green Full Zip Fleece Jakke', 'Adicross Evolution', 'GoToPolo', 'GoToPrimeGreenPique', 'Performance PrimeGreen'])
    if optionShoes in running:
        st.write(optionShoes)
        imageTags = optionShoes
    #else:
    #st.write('nothing')

def upload(file, **options):
    st.write('')




if st.button('SUBMIT'):
    st.write('The image is being uploaded to the cloud wth the corrected classification')
    #cloudinary.uploader.upload(image)
