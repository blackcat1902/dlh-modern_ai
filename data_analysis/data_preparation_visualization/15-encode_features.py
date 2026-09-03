#!/usr/bin/env python3
"""This module provides functions for cleaning
and preprocessing dataset features."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode dataset features using LabelEncoder for 'Churn',
    OrdinalEncoder for binary columns and 'TenureGroup',
    and One-Hot encoding for nominal features."""
    label_encoder = preprocessing.LabelEncoder()
    df['Churn'] = label_encoder.fit_transform(df['Churn'])

    ordinal_cols = ["Partner", "Dependents",
                    "PaperlessBilling", "SeniorCitizen"]
    ordinal_encoder = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']])
    for col in ordinal_cols:
        df[[col]] = ordinal_encoder.fit_transform(df[[col]]).astype(int)

    tenure_ordinal_encoder = preprocessing.OrdinalEncoder()
    df[['TenureGroup']] = tenure_ordinal_encoder.fit_transform(
        df[['TenureGroup']]).astype(int)

    onehot_encoder = preprocessing.OneHotEncoder(
        drop='first', sparse_output=False)
    onehot_cols = ["Contract", "PaymentMethod"]
    encoded = onehot_encoder.fit_transform(df[onehot_cols])

    df[onehot_encoder.get_feature_names_out(onehot_cols)] = encoded
    df = df.drop(columns=onehot_cols)

    return df, label_encoder, ordinal_encoder, tenure_ordinal_encoder
