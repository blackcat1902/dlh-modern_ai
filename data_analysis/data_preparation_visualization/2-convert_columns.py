#!/usr/bin/env python3
"""
Learn how to convert cols in the DataFrame to  appropriate data type.
"""
import pandas as pd


def convert_columns(df):
    """
    The modified DataFrame with converted column types.
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

    return df
