#!/usr/bin/env python3
""" Module for comparing numeric feature distributions by churn status.
"""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Plot overlapping histograms of a numeric column split by Churn.

    Args:
        df : DataFrame containing a 'Churn' column.
        col : Name of the numeric column.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    churn_no = df[df['Churn'] == 'No'][col]
    churn_yes = df[df['Churn'] == 'Yes'][col]

    plt.hist([churn_no, churn_yes], bins=30, label=['No', 'Yes'])

    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
    return None