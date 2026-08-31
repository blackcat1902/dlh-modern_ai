#!/usr/bin/env python3
"""
Chain separable blocks into a full backbone
"""
from tensorflow import keras
depthwise_separable_conv = __import__(
    '4-depthwise_separable_conv').depthwise_separable_conv


def mobilenet_backbone(inputs):
    """
    Builds the MobileNetV1 feature extractor:
    an initial strided convolution followed by
    a stack of depthwise separable conv blocks,
    downsampling at specific stages
    """
    x = keras.layers.Conv2D(
        32, 3, strides=2, padding='same')(inputs)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.ReLU()(x)

    layer_config = [
        (64, 1),
        (128, 2),
        (128, 1),
        (256, 2),
        (256, 1),
        (512, 2),
        (512, 1),
        (512, 1),
        (512, 1),
        (512, 1),
        (512, 1),
        (1024, 2),
        (1024, 1),
    ]

    for filters, stride in layer_config:
        x = depthwise_separable_conv(x, filters, stride)

    return x
