#!/usr/bin/env python3
"""Module that provides a function to build a Decision Tree Classifier."""
from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """Build and return a DecisionTreeClassifier instance.

    Args:
        min_samples_leaf (int): Min samples at a leaf node.
        min_samples_split (int): Min samples to split an internal node.
        random_state (int): Seed for reproducibility.

    Returns:
        tree.DecisionTreeClassifier: The configured decision tree model.
    """
    model = tree.DecisionTreeClassifier(
        criterion='gini',
        min_samples_leaf=min_samples_leaf,
        min_samples_split=min_samples_split,
        random_state=random_state
    )
    return model
