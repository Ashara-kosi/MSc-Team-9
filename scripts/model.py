#28, 28, 1
# Importing required libs
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Loading model
model = load_model("asl_lstm_model5.h5")


# Preparing and pre-processing the image
def preprocess_img(img_path):
    op_img = Image.open(img_path)
    img_resize = op_img.resize((28, 28))
    img2arr= np.array(img_resize, dtype=np.float32)
    #img2arr = img_to_array(img_resize) / 255.0
    img3arr = img2arr[:,:,0]
    img_reshape = img3arr.reshape(1, 28, 28, 1)
    return img_reshape


# Predicting function
def predict_result(predict):
    pred = model.predict(predict)
    return np.argmax(pred[0], axis=-1)

def predict_result(predict):
    pred = model.predict(predict)
    pred_string = np.argmax(pred[0], axis=-1)
    character = ''
    if pred_string == 0:
        character = 'Comfortable'
    elif pred_string == 1:
        character = 'Bored'
    else:
        character = 'Annoy'
    return character

