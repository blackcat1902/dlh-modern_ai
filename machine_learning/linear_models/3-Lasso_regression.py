#!/usr/bin/env python3
"""Defines a function that creates a Lasso Regression model."""
from sklearn import linear_model


def lasso_regression(random_state):
    """Creates a Lasso Regression model with L1 regularization
    for automatic feature selection.

    Args:
        random_state (int): Seed for reproducibility.

    Returns:
        model: An untrained Lasso regression model.
    """
    model = linear_model.Lasso(random_state=random_state)
    return model
