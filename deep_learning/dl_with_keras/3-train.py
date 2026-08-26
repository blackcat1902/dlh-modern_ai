#!/usr/bin/env python3
"""
Train keras model
"""


def train_model(model, X, Y, epochs, verbose=1):
    """
    Write a function train_model that trains a Keras model.
    """
    model.fit(
        X, Y,
        epochs=epochs,
        verbose=verbose
    )
