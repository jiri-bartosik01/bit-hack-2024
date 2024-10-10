from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dataclasses import dataclass
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace with a specific domain for better security.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.).
    allow_headers=["*"],  # Allows all headers.
)

@dataclass
class Pool:
    id: int
    opening_hours: list[int]
    data: list[int]

pools = [
    Pool(0, [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],[]),
    Pool(1, [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 21],[]),
    Pool(2, [6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20, 21,22],[]),
    Pool(3, [8,9,10,11,12,13,14,15,16,17,18,19,20],[]),
    Pool(4, [8,9,10,11,12,13,14,15,16,17,18,19,20, 21],[])
]

model = load_model('model.keras')

@app.get("/predictions/{id}")
async def graph(id: int):
    # use the neural network to predict
    pool = pools[id]
    # get current year by using some library
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    temp = 17.0

    for i in range(len(pool.opening_hours)):
        input_data = np.array([id, year, month, day, pool.opening_hours[i], temp])
        sequence_input = np.tile(input_data, (168, 1))
        sequence_input = sequence_input.reshape((1, 168, 6))
        prediction = model.predict(sequence_input)
        print(f"Predicted total: {prediction[0][0]}")
        pool.data.append(int(prediction[0][0]))

    return pool