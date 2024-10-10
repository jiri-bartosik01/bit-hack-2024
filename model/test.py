#!env/bin/python3

import tensorflow as tf
from tensorflow.keras.models import load_model

from data import train_X, test_X, train_y, test_y

# Load the model
model = load_model('model.keras')

# Test the model
predictions = model.predict(tf.convert_to_tensor(test_X, dtype=tf.float32))
loss, mae = model.evaluate(tf.convert_to_tensor(test_X, dtype=tf.float32), test_y)

pool = 0
year = 2024
month = 10
day = 10
hour = 12
temp = 24.0

prediction = model.predict(tf.convert_to_tensor([[[pool, year, month, day, hour, 0, temp]]], dtype=tf.float32))

print(f'Prediction: {prediction}')

print(f'Test Loss: {loss}')
print(f'Test MAE: {mae}')
print(f'Predictions: {predictions[:5]}')
print(f'Actual: {test_y[:5]}')
