#!/usr/bin/env python3
"""
Split a convolution into two cheaper ones
"""
from tensorflow import keras


def depthwise_separable_conv(X, filters, stride=1):
    """
    Applies a depthwise convolution followed by a
    pointwise convolution, each with Batch
    Normalization and ReLU activation
    """
    x = keras.layers.DepthwiseConv2D(
        3, strides=stride, padding='same')(X)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.ReLU()(x)

    x = keras.layers.Conv2D(filters, 1)(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.ReLU()(x)

    return x
