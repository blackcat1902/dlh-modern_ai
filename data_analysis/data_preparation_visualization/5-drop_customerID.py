#!/usr/bin/env python3
import pandas as pd
def drop_customerID(df):
    df = df.drop(columns=['customerID'])
    return df
