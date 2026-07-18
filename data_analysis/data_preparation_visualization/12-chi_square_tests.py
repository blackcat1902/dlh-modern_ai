#!/usr/bin/env python3
"""
Module for performing Chi-square tests on categorical features
to evaluate independence with the target variable 'Churn'.
"""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Perform Chi-square tests between each categorical feature and Churn.

    Args:
        df (pd.DataFrame): DataFrame containing 'Churn' and categorical columns.

    Returns:
        dict: {feature_name: p_value}
    """
    results = {}
    target = 'Churn'

    for col in df.columns:
        if col == target:
            continue

        contingency_table = pd.crosstab(df[col], df[target])
        chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)

        results[col] = p_value

    return results
