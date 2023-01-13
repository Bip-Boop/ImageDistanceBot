import abc

import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.models import Model
from tensorflow.keras.applications import vgg16, inception_v3
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions

class ImageClassifier(abc.ABC):

    @abc.abstractmethod
    def conscious_prediction(self, filename):
        pass

    @abc.abstractmethod
    def subconscious_prediction(self, filename):
        pass

    @abc.abstractmethod
    def classification_prediction(self, filename):
        pass


class VGGClassifier(ImageClassifier):

    def __init__(self):
        self.vgg_model = vgg16.VGG16(weights='imagenet')
        self.vgg_cut = Sequential()
        for layer in self.vgg_model.layers[:-1]:
            self.vgg_cut.add(layer)
    
    def process_image(self, filename):
        # load an image in PIL format
        original = load_img(filename, target_size=(224, 224))
        # convert the PIL image to a numpy array
        # IN PIL - image is in (width, height, channel)
        # In Numpy - image is in (height, width, channel)
        numpy_image = img_to_array(original)
        # Convert the image / images into batch format
        # expand_dims will add an extra dimension to the data at a particular axis
        # We want the input matrix to the network to be of the form (batchsize, height, width, channels)
        # Thus we add the extra dimension to the axis 0.
        image_batch = np.expand_dims(numpy_image, axis=0)

        # prepare the image for the VGG model
        processed_image = vgg16.preprocess_input(image_batch.copy())
        return processed_image


    def subconscious_prediction(self, filename):
        
        processed_image = self.process_image(filename)
        predictions_cut = self.vgg_cut.predict(processed_image)
        return predictions_cut[0]

    def conscious_prediction(self, filename):
        
        processed_image = self.process_image(filename)
        predictions = self.vgg_model.predict(processed_image)
        return predictions[0]

    def classification_prediction(self, filename):

        processed_image = self.process_image(filename)

        # get the predicted probabilities for each class
        predictions = self.vgg_model.predict(processed_image)
        label_vgg = decode_predictions(predictions)
        return label_vgg[0][0][1]

class InceptionClassifier(ImageClassifier):

    def __init__(self):
        self.inception_model = inception_v3.InceptionV3(weights='imagenet')
        output = self.inception_model.layers[-2].output
        self.inception_cut = Model(inputs = self.inception_model.input, outputs = output)
    
    def process_image(self, filename):
        # load an image in PIL format
        original = load_img(filename, target_size=(299, 299))

        # Convert the PIL image into numpy array
        numpy_image = img_to_array(original)

        # reshape data in terms of batchsize
        image_batch = np.expand_dims(numpy_image, axis=0)

        # prepare the image for the Inception model
        processed_image = inception_v3.preprocess_input(image_batch.copy())
        return processed_image


    def subconscious_prediction(self, filename):
        
        processed_image = self.process_image(filename)
        predictions_cut = self.inception_cut.predict(processed_image)
        return predictions_cut[0]

    def conscious_prediction(self, filename):
        
        processed_image = self.process_image(filename)
        predictions = self.inception_model.predict(processed_image)
        return predictions[0]

    def classification_prediction(self, filename):
        processed_image = self.process_image(filename)

        # get the predicted probabilities for each class
        predictions = self.inception_model.predict(processed_image)
        label_vgg = decode_predictions(predictions)
        return label_vgg[0][0][1]