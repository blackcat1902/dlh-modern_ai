#!/usr/bin/env python3
"""
Unfreezes the last n_layers of the base CNN model.
"""


def unfreeze_top_layers(model, n_layers):
    """
    Unfreeze the last n_layers of the model's
    base CNN
    """

    for layer in model.layers:
        layer.trainable = False

    if n_layers > 0:
        for layer in model.layers[-n_layers:]:
            layer.trainable = True
            