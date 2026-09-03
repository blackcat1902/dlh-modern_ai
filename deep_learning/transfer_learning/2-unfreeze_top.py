#!/usr/bin/env python3
"""
Unfreezes the last n_layers of the base CNN model.
"""


def unfreeze_top_layers(model, n_layers):
    """
    Unfreezes the last n_layers of the base CNN model inside the main model.
    """
    base_model = model.layers[0]
    base_model.trainable = True

    if n_layers <= 0:
        for layer in base_model.layers:
            layer.trainable = False
        return

    split_index = len(base_model.layers) - n_layers

    # Freeze earlier layers
    for layer in base_model.layers[:split_index]:
        layer.trainable = False

    # Unfreeze top layers
    for layer in base_model.layers[split_index:]:
        layer.trainable = True
        