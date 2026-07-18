#!/usr/bin/env python3
""" Module for plotting the distribution of the target variable Churn. """

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """ Plot a bar chart of churn class distribution.

    Args:
        df (pandas.DataFrame): DataFrame containing a 'Churn' column.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    churn_counts = df['Churn'].value_counts()
    churn_counts = churn_counts.reindex(['No', 'Yes'])

    colors = ['skyblue', 'salmon']

    plt.bar(churn_counts.index, churn_counts.values, color=colors)

    plt.ylabel('Count')
    plt.title('Churn Distribution')
    plt.show()

    return None