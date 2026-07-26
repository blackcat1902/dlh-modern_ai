#!/usr/bin/env python3
"""Decision Tree Classifier module"""
from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """
    Creates and configures a Scikit-learn DecisionTreeClassifier instance.

    Args:
        min_samples_leaf (int): Minimum number of samples required at a leaf node.
        min_samples_split (int): Minimum number of samples required to split an internal node.
        random_state (int): Seed used by the random number generator.

    Returns:
        tree.DecisionTreeClassifier: Configured Decision Tree model.
    """
model = tree.DecisionTreeClassifier(
        criterion='gini',
        min_samples_leaf=min_samples_leaf,
        min_samples_split=min_samples_split,
        random_state=random_state
    )
    return model
