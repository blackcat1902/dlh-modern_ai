import pandas as pd
#!/usr/bin/env python3
def convert_columns(df):
    # TotalCharges: boşlukları NaN yap
    df['TotalCharges'] = df['TotalCharges'].replace(" ", pd.NA)

    # TotalCharges: numeric'e çevir
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # SeniorCitizen: replace ile dönüştür (senin istediğin yol)
    df['SeniorCitizen'] = df['SeniorCitizen'].replace({0: "No", 1: "Yes"})

    return df
