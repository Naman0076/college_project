import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

def prepare_data(df, feature='temperature', time_steps=10):
    scaler = MinMaxScaler()
    values = scaler.fit_transform(df[[feature]])

    X, y = [], []
    for i in range(len(values) - time_steps):
        X.append(values[i:i + time_steps])
        y.append(values[i + time_steps])
    return np.array(X), np.array(y), scaler

def train_and_predict(df):
    X, y, scaler = prepare_data(df)

    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(64, return_sequences=True, input_shape=(X.shape[1], 1)),
        tf.keras.layers.LSTM(32),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=10, batch_size=8, verbose=0)

    prediction = model.predict(X)
    return scaler.inverse_transform(prediction), scaler.inverse_transform(y)