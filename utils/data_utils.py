from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img,img_to_array
from keras.applications.vgg16 import preprocess_input as preprocess_input_vgg
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input as preprocess_input_inc
import numpy as np
from pickle import dump,load

#MODEL = VGG16(include_top=False, pooling='avg')
MODEL=InceptionV3(include_top=False,pooling='avg')
PATH_IN = "C:/Users/akhil/DSP/Flicker Data/Flickr8k_text/Flickr_8k.trainImages.txt"
PATH_OUT_Inc = "C:/Users/akhil/PycharmProjects/Image-captioning---DSP/pkl files/inception_V3.pkl"
DATA_PATH = "C:/Users/akhil/DSP/Flicker Data/Flickr8k_Dataset/Flicker8k_Dataset"
PRE_PROCESS = preprocess_input_inc

img_feat_dict = {}


def get_img_feat(path_in, data_path, path_out, model, pre_process):

    TARGET_SIZE = (224, 224)

    with open(path_in)as f:
        train_img_data = f.read()

    for l in train_img_data.split('\n'):
        image_id = l.split('.')[0]
        # Loading individual images
        img = load_img(f"{data_path}/{image_id}.jpg", target_size=TARGET_SIZE)
        # Converting image to array
        img_array = img_to_array(img)
        # array shape - (224,224,3)
        n_img = pre_process(img_array)
        # Adding one more dimension to feed to model in batches
        n_img = np.expand_dims(n_img, axis=0)
        # Extracting features from image
        feat_vec = model.predict(n_img)
        # feat vec shape (1,512)
        img_feat_dict[image_id] = np.reshape(feat_vec, (1, -1))

    with open(path_out, 'wb') as f:
        dump(img_feat_dict, f)
"""
Write code to extract image features as train, test and split blocks
Also extract captions and make ready to be fed into LSTM

Data cleaning for text convert to lower case, remove special characters 
Create a corpus with all unique words in the captions
Step 1 Extract image features
Step 2 Clean up captions, create corpus
Step 3 Encode each caption with a start and stop seq token
Step 4 Map each word in corpus to a higher dimension vecto
Step 5 Train the LSTM
  
"""

