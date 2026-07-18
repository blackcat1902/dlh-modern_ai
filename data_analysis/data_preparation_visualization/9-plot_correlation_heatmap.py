#!/usr/bin/env python3
""" Module for plotting correlation heatmap """
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """ Plot an annotated correlation heatmap for numeric columns.

    Args:
        df : Input DataFrame.

    Returns:
        None
    """
    plt.figure(figsize=(6, 5))

    ndf = df.select_dtypes(include=['float64', 'int64'])
    corr_matrix = ndf.corr()

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm',
        vmin=-1,
        vmax=1
        )

    plt.title("Correlation Matrix")
    plt.show()