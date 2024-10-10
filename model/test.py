#!env/bin/python3

import tensorflow as tf
from tensorflow.keras.models import load_model

from data import train_X, test_X, train_y, test_y

# Load the model
model = load_model('model.keras')

# Test the model
predictions = model.predict(tf.convert_to_tensor(test_X, dtype=tf.float32))
loss, mae = model.evaluate(tf.convert_to_tensor(test_X, dtype=tf.float32), test_y)

print(f'Test Loss: {loss}')
print(f'Test MAE: {mae}')
print(f'Predictions: {predictions[:5]}')
print(f'Actual: {test_y[:5]}')
