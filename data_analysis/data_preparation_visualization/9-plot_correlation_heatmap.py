#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_correlation_heatmap(df):
    """Computes and visualizes the pairwise correlation of continuous numeric

    features.

    This function filters the input DataFrame for numeric columns, computes
    their Pearson correlation matrix, and generates a highly readable,
    annotated heatmap using a 'coolwarm' colormap. The color scale is strictly
    mapped from -1 to 1 to reflect the true strength of the correlations.

    Args:
        df (pd.DataFrame): The input pandas DataFrame containing the data
            to be analyzed.

    Returns:
        None: Displays the generated heatmap plot directly.
    """
    # Compute the correlation matrix for numeric columns only
    corr_matrix = df.corr(numeric_only=True)

    # Set up the matplotlib figure layout
    plt.figure(figsize=(10, 8))

    # Generate the annotated heatmap with configured constraints
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        vmin=-1,
        vmax=1,
        linewidths=0.5,
    )

    # Add descriptive title and adjust padding
    plt.title("Correlation Heatmap", fontsize=14, pad=15)

    # Render the plot
    plt.show()