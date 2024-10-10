#!env/bin/python3

import matplotlib.pyplot as plt

from model import *

# Train the model
history = model.fit(tf.convert_to_tensor(train_X, dtype=tf.float32), train_y, epochs=25, batch_size=32, validation_split=0.2)
# Save the model
model.save('model.keras')

plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.xlabel('Epoch')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.savefig("fig1")
plt.show()

plt.plot(history.history['mae'], label='train mae')
plt.plot(history.history['val_mae'], label='val mae')
plt.xlabel('Epoch')
plt.ylabel('Mean Absolute Error (MAE)')
plt.legend()
plt.savefig("fig2")
plt.show()