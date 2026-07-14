#!/usr/bin/env python3
def clean_total_charges(df, method='drop'):
    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])

    elif method == 'median':
        median_value = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median_value)

    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure']
        )

    return df
