import keras
from PIL import Image, ImageOps
import numpy as np
from keras.preprocessing import image
import streamlit as st

# # globalConfidence = 0


def teachable_machine_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file, compile=False)

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    predictionPerc = prediction*100
    #global confidence 
    confidence = np.amax(predictionPerc) 

    # confidencePerc(confidence)
    #st.write(np.argmax(prediction))
    return np.argmax(prediction),confidence # return position of the highest probability

# st.write(confidence)

# def confidencePerc():
#     st.write(confidence,"%")
    #globalConfidence = x

# def globalConfidenceFct():
#     st.write(globalConfidence, "%")