#!/usr/bin/env python3
""" Module for performing chi-square tests. """

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Perform chi-square test for independence between each categorical feature
    and the target variable 'Churn'.

    Args:
        df : DataFrame containing a 'Churn' column.

    Returns:
        dict: {feature_name: p_value} for each categorical feature.
    """
    results = {}

    features = [col for col in df.columns if
                df[col].dtype == 'object' and col != 'Churn']

    for feature in features:
        con_tab = pd.crosstab(df[feature], df['Churn'])
        chi2, p, dof, expected = stats.chi2_contingency(con_tab)
        results[feature] = p

    return results