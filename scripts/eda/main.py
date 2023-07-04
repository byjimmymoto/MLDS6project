# Augmentacion
import os, random
import seaborn as sns
# Librerías de utilidad para manipulación y visualización de datos.
from numbers import Number
import re
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from unidecode import unidecode
from IPython.display import display
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn

#Importamos tensorflow
import tensorflow as tf
tf.config.run_functions_eagerly(True)
# Ignorar warnings.
import warnings
warnings.filterwarnings('ignore')


def data_augmentation(X_train, y_train,
                      X_val, y_val,
                      X_test, y_test,
                      width_range, height_range, zoom_range, h_flip, fill):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)
    tf.keras.utils.set_random_seed(0)
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                                                        rescale=1./255,
                                                        width_shift_range=width_range,
                                                        height_shift_range=height_range,
                                                        zoom_range=zoom_range,
                                                        horizontal_flip=h_flip,
                                                        fill_mode=fill)
    val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

    X_train_aug = train_datagen.flow(X_train, y_train)
    X_val_aug = val_datagen.flow(X_val, y_val)
    X_test_aug = test_datagen.flow(X_test, y_test)

    return X_train_aug, X_val_aug, X_test_aug

# PreEntrenamiento
def pretrained_model(train_base_model, units, dropout):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)
    tf.keras.utils.set_random_seed(0)
    # definir el modelo Mobilenet
    extractor = tf.keras.applications.MobileNet(weights='imagenet', 
                                            include_top=False,
                                            input_shape=(224, 224, 3))
    # definir si congelamos el extractor de características
    for layer in extractor.layers:
      layer.trainable=train_base_model
    # crear una capa de pooling para consolidar los feature maps de salida en 
    # 1024 valores
    pool = tf.keras.layers.GlobalAveragePooling2D()(extractor.output)
    # agregar una capa densa
    dense = tf.keras.layers.Dense(units=units, activation="relu")(pool)
    # agregar dropout para regularización
    drop = tf.keras.layers.Dropout(dropout)(dense)
    # agrega una capa de salida
    output = tf.keras.layers.Dense(units=units, activation="softmax")(drop)
    # definimos nuestro modelo de transfer learning
    model = tf.keras.models.Model(inputs=[extractor.input], outputs=[output])
    # compilamos el modelo
    return model