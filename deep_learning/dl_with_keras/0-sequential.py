#!/usr/bin/env python3
"""
Build Model using Sequential
"""
from tensorflow import keras


def build_model(input_dim, neurons_h):
    """
    Use Sequential class
    """

    model = keras.Sequential(
        [
            keras.layers.Input(shape=(input_dim,)),
            keras.layers.Dense(neurons_h, activation='sigmoid'),
            keras.layers.Dense(10, activation='softmax')
        ]
    )

    return model