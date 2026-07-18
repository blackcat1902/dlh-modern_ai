#!/usr/bin/env python3
""" Module for plotting categorical feature distributions.
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """ Plot bar charts for categorical features in a grid layout.

    Args:
        df : Input DataFrame.
        columns_to_plot : List of column names to plot.
            If None, plots all object-type columns except 'Churn'.

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = [
            col for col in df.select_dtypes(include=['object']).columns
            if col != 'Churn'
        ]
    else:
        columns_to_plot = [col for col in columns_to_plot if col in df.columns]
    n_cols, n_rows = 3, (len(columns_to_plot) + 2) // 3
    if n_rows == 0:
        n_rows = 1

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))

    if n_rows == 1 and n_cols == 1:
        axes_flat = [axes]
    else:
        axes_flat = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        ax = axes_flat[i]
        counts = df[col].value_counts()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_title(col)
        ax.tick_params(axis='x', rotation=45)

    # Hide any unused subplots
    for j in range(i + 1, len(axes_flat)):
        axes_flat[j].set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()

    return None