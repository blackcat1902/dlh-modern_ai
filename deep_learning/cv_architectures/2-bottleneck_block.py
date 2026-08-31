#!/usr/bin/env python3
"""
Let information skip ahead
"""
from tensorflow import keras


def bottleneck_block(x, filters, stride=1, downsample=False, name=None):
    """
    Builds a ResNet bottleneck residual block with
    a 1x1 reduce, 3x3 conv and 1x1 expand,
    adding a shortcut connection to the input
    """
    shortcut = x

    y = keras.layers.Conv2D(
        filters, 1, strides=stride,
        name=f'{name}_conv1')(x)
    y = keras.layers.BatchNormalization(name=f'{name}_bn1')(y)
    y = keras.layers.ReLU(name=f'{name}_relu1')(y)

    y = keras.layers.Conv2D(
        filters, 3, padding='same',
        name=f'{name}_conv2')(y)
    y = keras.layers.BatchNormalization(name=f'{name}_bn2')(y)
    y = keras.layers.ReLU(name=f'{name}_relu2')(y)

    y = keras.layers.Conv2D(
        filters * 4, 1,
        name=f'{name}_conv3')(y)
    y = keras.layers.BatchNormalization(name=f'{name}_bn3')(y)

    if downsample:
        shortcut = keras.layers.Conv2D(
            filters * 4, 1, strides=stride,
            name=f'{name}_shortcut_conv')(shortcut)
        shortcut = keras.layers.BatchNormalization(
            name=f'{name}_shortcut_bn')(shortcut)

    output = keras.layers.Add(name=f'{name}_add')([y, shortcut])
    output = keras.layers.ReLU(name=f'{name}_out')(output)

    return output
