import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_categorical_vs_churn(df, col):
    """Visualizes the churn rate (proportion of 'Yes') for each category in a

    given column.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data and a 'Churn'
            column.
        col (str): The name of the categorical column to analyze against churn.

    Returns:
        None: Displays a bar plot showing churn rates per category.
    """
    # 1. Set the layout size to (12, 8) as requested
    plt.figure(figsize=(12, 8))

    # 2. Convert 'Churn' column to binary (1 for 'Yes', 0 for 'No')
    # Seaborn's barplot automatically calculates the mean of these 1s and 0s,
    # which directly gives the proportion/rate of churned customers.
    sns.barplot(
        x=col,
        y=(df["Churn"] == "Yes").astype(int),
        data=df,
        errorbar=None,  # Removes the error bar lines for a cleaner presentation
        palette="viridis",  # Aesthetic color palette for clear distinction
    )

    # 3. Set the y-axis label to "Churn Rate"
    plt.ylabel("Churn Rate", fontsize=12)

    # 4. Dynamically set the title using the requested format: "Churn Rate by <col>"
    plt.title(f"Churn Rate by {col}", fontsize=14, pad=15)

    # 5. Rotate the x-axis labels by 45 degrees to prevent text overlapping
    plt.xticks(rotation=45)

    # 6. Render and display the final plot
    plt.show()