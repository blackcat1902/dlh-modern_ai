#!/usr/bin/env python3
"""Computer Vision Architectures.
This module provides functions for building, customizing, and training
convolutional neural network (CNN) architectures in Keras."""
from tensorflow import keras


def create_cnn_model(input_shape, filters, kernel_sizes,
                     activations, pooling_type='max'):
    """Creates and compiles a Keras CNN model with
    customizable layers and pooling."""
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=input_shape))

    for f, k, a in zip(filters, kernel_sizes, activations):
        model.add(keras.layers.Conv2D(filters=f, kernel_size=k,
                                      activation=a))
        if pooling_type == 'max':
            model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        elif pooling_type == 'avg':
            model.add(keras.layers.AveragePooling2D(pool_size=(2, 2)))

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model
