#!/usr/bin/env python3
"""
Data duplication dropped ın the DataFrame
data integration
"""


def remove_duplicates(df):
    """droped duplicates cols."""

    return df.drop_duplicates()
