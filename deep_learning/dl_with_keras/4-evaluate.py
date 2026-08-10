#!/usr/bin/env python3
"""
Evaluate keras model

"""


def evaluate_model(model, X, Y, verbose=0):
    """
    A function evaluate_model(m) to assess a trained Keras model's performance on a given data.
    """

    loss, accuracy = model.evaluate(X, Y, verbose=verbose)

    return loss, accuracy