#!env/bin/python

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model


model = load_model('model.keras')


for i in range(24):
    input_data = np.array([[0, 2021, 1, 10, i, 0]])
    sequence_input = np.tile(input_data, (168, 1))
    sequence_input = sequence_input.reshape((1, 168, 6))
    prediction = model.predict(sequence_input)
    print(f"Predicted total: {prediction[0]}")

