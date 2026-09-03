#!/usr/bin/env python3
""" Module for plotting churn rate per category for a categorical column.
"""
import pandas as pd
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """
    Compare given column with Churn
    plotting churn rate
    """

    # Churn rate (Yes proportion) per category
    churn_rate = (df['Churn'] == 'Yes'
                  ).astype(int
                           ).groupby(df[col]
                                     ).mean()

    plt.figure(figsize=(12, 8))

    plt.bar(churn_rate.index, churn_rate.values)

    plt.title(f'Churn Rate by {col}')
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=45)

    plt.show()
