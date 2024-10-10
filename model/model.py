#!env/bin/python3

import tensorflow as tf
from tensorflow.keras import layers, models

from data import *

input_layer = layers.Input(shape=(window_size, train_X.shape[2]))

# Build the CNN model
model = models.Sequential([
    input_layer,
    layers.Conv1D(1024, kernel_size=3, padding='SAME', activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.Conv1D(512, kernel_size=3, padding='SAME', activation='relu'),
    layers.MaxPooling1D(pool_size=2),
    layers.Flatten(),
    layers.Dense(8192, activation='relu'),
    layers.Dense(2048, activation='relu'),
    layers.Dense(1024, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse', metrics=['mae'])

# Summary of the model
model.summary()
