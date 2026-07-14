#!/usr/bin/env python3
def remove_duplicates(df):
# Duplicate rows are removed. 
    df = df.drop_duplicates()
    return df
