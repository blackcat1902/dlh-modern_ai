#!/usr/bin/env python3
"""
Wrap the backbone with a classifier head
"""
from tensorflow import keras
mobilenet_backbone = __import__('5-mobilenet_backbone').mobilenet_backbone


def mobilenet(input_shape=(224, 224, 3), num_classes=1000):
    """
    Builds MobileNetV1: the backbone followed by
    global average pooling and a softmax
    classification layer
    """
    inputs = keras.Input(shape=input_shape)
    x = mobilenet_backbone(inputs)

    x = keras.layers.GlobalAveragePooling2D()(x)
    outputs = keras.layers.Dense(num_classes, activation='softmax')(x)

    return keras.Model(inputs, outputs, name='MobileNetV1')
