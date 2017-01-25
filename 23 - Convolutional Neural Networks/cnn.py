# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

classifier.fit_generator(training_set,
                         samples_per_epoch = 8000,
                         nb_epoch = 25,
                         validation_data = test_set,
                         nb_val_samples = 2000)

# Part 3 - Homework - Predict if your pet is a dog or a cat

import numpy as np
from keras.preprocessing import image as image_utils
 
test_image_1 = image_utils.load_img('dataset/test_image/cat.4001.jpg', target_size=(64, 64))
test_image_1 = image_utils.img_to_array(test_image_1)
test_image_1 = np.expand_dims(test_image_1, axis = 0)

test_image_2 = image_utils.load_img('dataset/test_image/cat.4002.jpg', target_size=(64, 64))
test_image_2 = image_utils.img_to_array(test_image_2)
test_image_2 = np.expand_dims(test_image_2, axis = 0)

test_image_3 = image_utils.load_img('dataset/test_image/cat.4003.jpg', target_size=(64, 64))
test_image_3 = image_utils.img_to_array(test_image_3)
test_image_3 = np.expand_dims(test_image_3, axis = 0)

test_image_4 = image_utils.load_img('dataset/test_image/cat.4004.jpg', target_size=(64, 64))
test_image_4 = image_utils.img_to_array(test_image_4)
test_image_4 = np.expand_dims(test_image_4, axis = 0)

test_image_5 = image_utils.load_img('dataset/test_image/cat.4005.jpg', target_size=(64, 64))
test_image_5 = image_utils.img_to_array(test_image_5)
test_image_5 = np.expand_dims(test_image_5, axis = 0)

test_image = image_utils.load_img('dataset/test_image/Hadelin_Dog.jpg', target_size=(64, 64))
test_image = image_utils.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
 
classifier.predict_on_batch(test_image_1)
classifier.predict_on_batch(test_image_2)
classifier.predict_on_batch(test_image_3)
classifier.predict_on_batch(test_image_4)
classifier.predict_on_batch(test_image_5)
classifier.predict_on_batch(test_image)