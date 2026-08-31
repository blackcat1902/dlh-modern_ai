#!/usr/bin/env python3
"""
Stack convolutions and let them see
"""
from tensorflow import keras


def create_cnn_model(input_shape, filters, kernel_sizes, activations,
                      pooling_type='max'):
    """
    Builds a CNN model from a list of
    filters, kernel_sizes and activations,
    applying a pooling layer after each
    convolutional layer
    """
    pooling_layer = (keras.layers.MaxPooling2D if pooling_type == 'max'
                      else keras.layers.AveragePooling2D)

    model = keras.Sequential()
    model.add(keras.Input(shape=input_shape))

    for i in range(len(filters)):
        filters_i = filters[i]
        kernel_size = kernel_sizes[i]
        activation = activations[i]

        model.add(keras.layers.Conv2D(
            filters_i, kernel_size, activation=activation))
        model.add(pooling_layer())

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(10))

    return model
