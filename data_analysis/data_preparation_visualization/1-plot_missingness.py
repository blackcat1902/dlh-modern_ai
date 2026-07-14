#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def plot_missingness(df):
    plt.figure(figsize=(12, 8))

    colm_name = list(df.columns)

    for i in range(len(colm_name)):
        col_name = colm_name[i]
        missing_rows = df[df[col_name].isna()].index
        plt.scatter(missing_rows, [i] * len(missing_rows), marker='|')

    plt.yticks(range(len(colm_name)), colm_name)
    plt.xlabel("Row Index")
    plt.ylabel("Columns")
    plt.title("Missingness Plot")
    plt.tight_layout()
    plt.show()
