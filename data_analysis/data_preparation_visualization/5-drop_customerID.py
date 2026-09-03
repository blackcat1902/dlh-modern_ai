#!/usr/bin/env python3
"""
Drop low variance value columns
"""


def drop_customerID(df):
    """drop the customerId col."""

    df = df.copy()

    df = df.drop(['customerID'], axis=1)
    return df
