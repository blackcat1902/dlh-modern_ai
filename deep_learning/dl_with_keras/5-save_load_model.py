#!/usr/bin/env python3
"""
to save and reload a Keras model, i
ncluding its architecture, weights, and optimizer state.

"""
from tensorflow import keras


def save_model(model, filepath):
    """
    the function that  to save a keras model
    """
    model.save(filepath)


def load_model(filepath):
    """
    the function that to load a keras model
    """
    return keras.models.load_model(filepath)
