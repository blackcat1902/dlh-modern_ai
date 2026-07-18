#!/usr/bin/env python3
"""
Plot continuous numerical feature distributions:
- Histogram + KDE
- Boxplot
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
    Plots histograms with KDE and boxplots for continuous numerical features.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing numeric columns.

    columns_to_plot : list, optional
        List of numeric columns to plot. If None, all numeric columns
        are selected automatically.

    Description
    -----------
    For each numeric column:
    - Left subplot: Histogram + KDE
        bins = 30
        density = True
        alpha = 0.7
        edgecolor = 'black'
        KDE line color = red
        Title: "<column_name> Histogram + KDE"

    - Right subplot: Boxplot
        Title: "<column_name> Boxplot"

    Returns
    -------
    None
        Displays the plot and saves it as Task_8.png.
    """

    # If user does not provide a list → select all numeric columns
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include=[np.number]).columns.tolist()

    # Number of numeric columns
    n_cols = len(columns_to_plot)

    # Create subplots: each row has 2 plots (histogram + boxplot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    # If only one numeric column → reshape axes
    if n_cols == 1:
        axes = axes.reshape(1, -1)

    # Loop through each numeric column
    for i, col in enumerate(columns_to_plot):

        # Extract data and drop NaN values
        data = df[col].dropna()

        # --- Histogram + KDE ---
        ax_hist = axes[i, 0]

        # Histogram
        ax_hist.hist(
            data,
            bins=30,
            density=True,
            alpha=0.7,
            edgecolor='black'
        )

        # KDE curve
        kde = stats.gaussian_kde(data)
        x_vals = np.linspace(data.min(), data.max(), 500)
        ax_hist.plot(x_vals, kde(x_vals), color='red')

        ax_hist.set_title(f"{col} Histogram + KDE")

        # --- Boxplot ---
        ax_box = axes[i, 1]
        ax_box.boxplot(data, vert=True)
        ax_box.set_title(f"{col} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
