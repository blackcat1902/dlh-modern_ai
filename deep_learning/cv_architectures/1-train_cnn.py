#!/usr/bin/env python3
"""
Feed the network and watch it learn
"""
from tensorflow import keras


def compile_and_train_cnn(model, epochs, batch_size, x_train, y_train,
                           x_val, y_val, optimizer_name='adam',
                           optimizer_params=None):
    """
    Compiles a CNN model with the given optimizer
    and trains it on the provided data,
    validating on a separate validation set
    """
    if optimizer_params is None:
        optimizer_params = {}

    optimizers = {
        'adam': keras.optimizers.Adam,
        'sgd': keras.optimizers.SGD,
        'rmsprop': keras.optimizers.RMSprop
    }
    optimizer = optimizers[optimizer_name](**optimizer_params)

    model.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    history = model.fit(
        x_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(x_val, y_val)
    )

    return model, history
