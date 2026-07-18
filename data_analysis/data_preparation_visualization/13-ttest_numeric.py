#!/usr/bin/env python3
import pandas as pd
from scipy import stats


def ttest_numeric(df):
    """Performs Welch's t-tests for continuous numeric features against the Churn

    status.

    This function separates the dataset into two distinct groups based on the
    'Churn' column ('Yes' vs 'No'). It then iterates through all continuous
    numeric features and calculates the p-value using Welch's t-test (which
    does not assume equal population variances) to determine if the means
    between the two groups are significantly different.

    Args:
        df (pd.DataFrame): The input DataFrame containing numeric features and a
          'Churn' column.

    Returns:
        dict: A dictionary where keys are feature names and values are the
        corresponding t-test p-values.
    """
    # Separate the dataset into two distinct groups based on Churn status
    churn_yes = df[df["Churn"] == "Yes"]
    churn_no = df[df["Churn"] == "No"]

    # Identify all continuous numeric columns in the DataFrame
    numeric_cols = df.select_dtypes(include=["number"]).columns

    # Initialize an empty dictionary to store the results
    results = {}

    # Perform Welch's t-test for each numeric column
    for col in numeric_cols:
        # equal_var=False specifies Welch's t-test instead of the standard Student's t-test
        t_stat, p_value = stats.ttest_ind(
            churn_yes[col], churn_no[col], equal_var=False
        )

        # Map the feature name to its calculated p-value
        results[col] = p_value

    return results
