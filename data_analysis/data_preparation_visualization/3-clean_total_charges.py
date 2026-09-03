#!/usr/bin/env python3
"""
Handles missing values in a column of the DataFrame
"""


def clean_total_charges(df, method='drop'):
    """Handles missings in total_charges field"""
    df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        median_value = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median_value)
    elif method == 'impute':
        impute_charge = df['MonthlyCharges'] * df['tenure']
        df['TotalCharges'] = df['TotalCharges'].fillna(impute_charge)

    return df
