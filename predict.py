from keras_preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np

# path = input("Enter the image path : ")
# path = path.replace('\','\\')


# C:\\Users\\hp\\Desktop\\X-Ray\\chest_xray\\chest_xray\\test\\NORMAL\\NORMAL2-IM-0307-0001.jpeg - Normal



def Predict(path):
	model=load_model('XPNEUMONIA.h5') #Loading our model
	img=image.load_img(path,target_size=(224,224))
	imagee=image.img_to_array(img) #Converting the X-Ray into pixels
	imagee=np.expand_dims(imagee, axis=0)
	img_data=preprocess_input(imagee)
	prediction=model.predict(img_data)
	if prediction[0][0]>prediction[0][1]: #Printing the prediction of model.
		print(prediction)
		return 'Person is safe.'
	else:
		print(prediction)
		return 'Person is affected with Pneumonia.'
