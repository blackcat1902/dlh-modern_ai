#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_numeric_vs_churn(df, col):
    """Compares continuous numeric feature distributions between Churn categories

    using overlapping histograms.

    Args:
        df (pd.DataFrame): The input DataFrame containing the numeric column and
          a 'Churn' column.
        col (str): The name of the continuous numeric column to visualize.

    Returns:
        None: Displays the generated overlapping histogram plot.
    """
    # 1. Grafik alanının boyutunu (12, 8) olarak ayarla
    plt.figure(figsize=(12, 8))

    # 2. Üst üste binen (overlapping) histogramları çiz
    # Churn durumuna göre gruplamak için 'hue' parametresine 'Churn' veriyoruz
    # element="step" veya common_norm=False gibi detaylar seaborn sürümlerine göre
    # ve referans grafiğe göre hafif değişebilir ama standart net görünüm budur:
    sns.histplot(
        data=df,
        x=col,
        hue="Churn",
        bins=30,  # Veriyi x ekseninde 30 gruba böl
        element="bars",  # Standart bar görünümü
        multiple="layer",  # Üst üste binen katmanlar şeklinde göster
        alpha=0.5,  # Arkadaki barlar da görünsün diye yarı saydamlık ekle
    )

    # 3. Dinamik başlık ve x ekseni isimlendirmesi
    plt.title(f"{col} Distribution by Churn", fontsize=14, pad=15)
    plt.xlabel(col, fontsize=12)
    plt.ylabel("Count", fontsize=12)

    # 4. Gösterge (Legend) başlığı ve grafiği ekrana basma
    # Seaborn histplot otomatik legend ekler, başlığını güncellemek istersen:
    plt.gca().get_legend().set_title("Churn")

    plt.show()