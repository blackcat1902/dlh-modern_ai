#!/usr/bin/env python3
def drop_customerID(df):
    df = df.drop(columns=['customerID'])
    return df
