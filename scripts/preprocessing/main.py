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


# Compilar Modelo
def compile_model(model, l_r, metrics):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)
    tf.keras.utils.set_random_seed(0)
    # Ingrese su código aquí
    model.compile(loss="categorical_crossentropy", 
                  optimizer=tf.optimizers.Adam(learning_rate=l_r), 
                  metrics=metrics)
   
    return model

# Entrenar Modelo
def train_model(model, train_gen, val_gen, epochs, weights, batch_size):
    # Fijamos una semilla para efectos de reproducibiidad
    np.random.seed(0)    
    tf.keras.utils.set_random_seed(0)
    # Complete el código desde aquí:
    steps = len(train_gen)-1
    validations = len(val_gen)-1
    # Definimos el callback
    best_callback = tf.keras.callbacks.ModelCheckpoint(filepath=weights, 
                                                      monitor="val_loss", 
                                                      verbose=True, 
                                                      save_best_only=True,
                                                      save_weights_only=True, 
                                                      mode="min")
    # Entrenamos el modelo
    history = model.fit(x=train_gen, validation_data=val_gen, epochs=epochs, 
                        steps_per_epoch=steps, batch_size=batch_size,
                        validation_steps=validations,
                        callbacks=[best_callback])
    return model, history

