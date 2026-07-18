#!/usr/bin/env python3
""" Module for plotting churn rate per category for a categorical column.
"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """ Plot churn rate per category in a categorical column.

    Args:
        df : DataFrame containing a 'Churn' column.
        col : Name of the categorical column to analyze.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))
    churn_rates = df.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean())
    plt.bar(churn_rates.index, churn_rates.values, width=0.8)
    plt.title(f"Churn Rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.show()
    return None
    