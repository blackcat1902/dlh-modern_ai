#!/usr/bin/env python3
"""
Chi-square tests for categorical features vs Churn.
"""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Compute Chi-square p-values for categorical columns only.

    Args:
        df (pd.DataFrame): DataFrame containing Churn and categorical columns.

    Returns:
        dict: {feature_name: p_value}
    """

    results = {}
    target = 'Churn'

    # Select only categorical columns
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns

    for col in categorical_cols:
        if col == target:
            continue

        contingency_table = pd.crosstab(df[col], df[target])
        _, p_value, _, _ = stats.chi2_contingency(contingency_table)

        results[col] = p_value

    return results
