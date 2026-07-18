#!/usr/bin/env python3
"""
"""
import matplotlib.pyplot as plt

def plot_churn_distribution(df):
    """
    Plots the distribution of the Churn variable.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a 'Churn' column with values 'Yes' and 'No'.

    Description
    -----------
    Generates a bar plot showing the count of each Churn class.
    The bars are colored skyblue for 'No' and salmon for 'Yes'.
    The plot size is fixed to match the reference figure (12x8).

    Returns
    -------
    None
        The function displays the plot and does not return any value.
    """

    plt.figure(figsize=(12, 8))

    # Ensure the order is always ['No', 'Yes']
    counts = df['Churn'].value_counts().loc[['No', 'Yes']]

    plt.bar(counts.index, counts.values,
            color=['skyblue', 'salmon'])

    plt.title("Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Count")

    plt.show()
