#!/usr/bin/env python3
"""
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Plots bar charts for categorical feature distributions.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing categorical columns.

    columns_to_plot : list, optional
        List of categorical columns to plot. If None, all object-type
        columns except 'Churn' are selected automatically.

    Description
    -----------
    Generates bar plots for each categorical feature in a grid layout.
    X-axis labels are rotated by 45 degrees for readability.
    The plot layout matches the reference figure exactly.

    Returns
    -------
    None
        Displays the plot and saves it as Task_7.png.
    """

    # If user does not provide a list → select all object columns except Churn
    if columns_to_plot is None:
        columns_to_plot = [
            col for col in df.columns
            if df[col].dtype == 'object' and col != 'Churn'
        ]
    else:
        # If user provides a list → filter out invalid columns + Churn
        columns_to_plot = [
            col for col in columns_to_plot
            if col in df.columns and col != 'Churn'
        ]

    # Grid layout: 3 columns, dynamic number of rows
    n_cols = 3
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()

    # Plot each categorical column
    for ax, col in zip(axes, columns_to_plot):
        counts = df[col].value_counts()
        ax.bar(counts.index, counts.values, color='skyblue')
        ax.set_title(col)
        ax.set_xticklabels(counts.index, rotation=45)

    # Hide unused axes
    for ax in axes[len(columns_to_plot):]:
        ax.axis('off')

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
