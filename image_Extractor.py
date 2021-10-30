# #MUST READ!!

# #In order to download the files after cleanup -> run in terminal: wget -i images_cleaned_up.txt
# #This will download all images in the same folder with the .txt file


# #https://towardsdatascience.com/a-step-by-step-tutorial-to-build-and-deploy-an-image-classification-api-95fa449f0f6a


# class ImagePredictor:
#     def __init__(
#         self, model_path, resize_size, targets, pre_processing_function=preprocess_input
#     ):
#         self.model_path = model_path
#         self.pre_processing_function = pre_processing_function
#         self.model = load_model(self.model_path)
#         self.resize_size = resize_size
#         self.targets = targets
#     @classmethod
#     def init_from_config_path(cls, config_path):
#         with open(config_path, "r") as f:
#             config = yaml.load(f, yaml.SafeLoader)
#         predictor = cls(
#             model_path=config["model_path"],
#             resize_size=config["resize_shape"],
#             targets=config["targets"],
#         )
#         return predictor
#     @classmethod
#     def init_from_config_url(cls, config_path):
#         with open(config_path, "r") as f:
#             config = yaml.load(f, yaml.SafeLoader)
#         download_model(
#             config["model_url"], config["model_path"], config["model_sha256"]
#         )
#         return cls.init_from_config_path(config_path)
#     def predict_from_array(self, arr):
#         arr = resize_img(arr, h=self.resize_size[0], w=self.resize_size[1])
#         arr = self.pre_processing_function(arr)
#         pred = self.model.predict(arr[np.newaxis, ...]).ravel().tolist()
#         pred = [round(x, 3) for x in pred]
#         return {k: v for k, v in zip(self.targets, pred)}
#     def predict_from_file(self, file_object):
#         arr = read_from_file(file_object)
#         return self.predict_from_array(arr)

#im = Image.open("/Users/alexandru-robertcroitoru/Downloads/adidas_Superstar_LacelessFV3017.jpg")
#import Image, numpy
#numpy.asarray(Image.open('/Users/alexandru-robertcroitoru/Downloads/adidas_Superstar_LacelessFV3017.jpg').convert('L'))

# from PIL import Image
# from numpy import array
# im_1 = Image.open(r"/Users/alexandru-robertcroitoru/Downloads/adidas_Superstar_LacelessFV3017.jpg")
# ar = array(im_1)
# print(ar)

# from keras.models import load_model

# classifier=load_model('/Users/alexandru-robertcroitoru/VSCode/MasterThesis/Master-Thesis---Image-Classifier/keras_model.h5')

# classifier.summary()

# import h5py, numpy as np
# h5f=h5py.File('keras_model.h5','w')

# ds_data = np.random.random(100).reshape(10,10)
# group1 = h5f.create_group('group1')
# group1.create_dataset('ds_1', data=ds_data)
# group1.create_dataset('ds_2', data=ds_data)
# group1.create_dataset('ds_3', data=ds_data)

# print ('number of datasets in group:', len(group1))
# for (dsname, dsvalue) in group1.items() :
#     print ('for',dsname,':')
#     print ('shape:',dsvalue.shape)
#     print ('dtype:',dsvalue.dtype)

# h5f.close()

import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#reading the image 
image = mpimg.imread('/Users/alexandru-robertcroitoru/VSCode/MasterThesis/Data received/Running/Shoes/Runfalcon 2.0/FY5943_b2b021_pdp.jpg')
plt.imshow(image)


