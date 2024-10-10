#!env/bin/python3

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the dataset (assuming 'testdata' is a CSV file)
file_path = 'testdata'  # Update if necessary to match the actual format
data = pd.read_csv(file_path)

# Assume 'data' is a Pandas DataFrame containing your features
scaler = StandardScaler()
data[['capacity', 'temperature', 'humidity', 'wspeed']] = scaler.fit_transform(
    data[['capacity', 'temperature', 'humidity', 'wspeed']]
)

# Use pandas to one-hot encode categorical features
data = pd.get_dummies(data, columns=['day', 'isholiday'])

def create_time_windows(df, window_size=7):
    X, y = [], []
    for i in range(len(df) - window_size):
        X.append(df.iloc[i:i + window_size].values)
        y.append(df.iloc[i + window_size]['capacity'])  # Target is the capacity on the next day
    return np.array(X), np.array(y)

window_size = 3  # Number of days in each window
X, y = create_time_windows(data, window_size)

# Split into 70% training and 30% test
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, shuffle=False)