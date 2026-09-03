#!/usr/bin/env python3
""" Module for comparing numeric feature distributions by churn status.
"""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Plots side-by-side histograms
    """
    plt.figure(figsize=(12, 8))

    no_churn = df[df['Churn'] == 'No'][col]
    yes_churn = df[df['Churn'] == 'Yes'][col]

    plt.hist([no_churn, yes_churn], bins=30, label=['No', 'Yes'])

    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(f'{col}')
    plt.legend(title='Churn')

    plt.show()
    