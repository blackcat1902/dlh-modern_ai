#!/usr/bin/env python3
"""Module for feature engineering on the Telco Customer Churn dataset.

This module provides functionality to create consolidated and binned features
to improve model performance and remove redundant original columns.
"""
import pandas as pd


def create_features(df):
    """Engineers new features (NumServices, TenureGroup) and drops old ones.

    Args:
        df (pd.DataFrame): The input DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame with newly engineered features.
    """
    # 1. Define the service columns to evaluate (excluding PhoneService)
    service_cols = [
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]

    # Create a temporary DataFrame to calculate total active services
    temp_services = pd.DataFrame(index=df.index)

    for col in service_cols:
        if col == "InternetService":
            # Count 'DSL' and 'Fiber optic' as active subscriptions
            temp_services[col] = df[col].isin(["DSL", "Fiber optic"])
        else:
            # Count standard 'Yes' values as active subscriptions
            temp_services[col] = df[col] == "Yes"

    # Sum horizontally to get the total number of services per customer
    df["NumServices"] = temp_services.sum(axis=1)

    # 2. Bin the tenure column into specified categorical intervals
    # Intervals: 0-12, 13-24, 25-48, 49-60, 60+ (0 excluded, upper bounds inc)
    bins = [0, 12, 24, 48, 60, float("inf")]
    labels = ["0-12", "13-24", "25-48", "49-60", "60+"]

    df["TenureGroup"] = pd.cut(
        df["tenure"], bins=bins, labels=labels, right=True
    )

    # 3. Drop the original columns used to create the new engineered features
    cols_to_drop = service_cols + ["tenure"]
    df = df.drop(columns=cols_to_drop)

    return df
