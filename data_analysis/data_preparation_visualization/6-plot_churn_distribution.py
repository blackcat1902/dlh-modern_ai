#!/usr/bin/env python3
""" Module for plotting the distribution of the target variable Churn. """
import matplotlib.pyplot as pl


def plot_churn_distribution(df):
    """plotting churn distb."""
    plt.figure(figsize=(12, 8))
    plt.title('Churn Distribution')
    plt.ylabel('Count')

    colour_map = {'yes': 'salmon', 'no': 'skyblue'}

    counts = df['Churn'].value_counts()
    colours = counts.index.str.lower().map(colour_map)

    plt.bar(counts.index, counts.values, color=colours)
    plt.savefig('churn_dist')
    plt.show()
