"""
09_groupby_analysis.py
=======================
Soal 9: Gunakan groupby untuk mencari rata-rata (mean) total_sales
dan total quantity terjual per category dan per kota.
Kota & kategori mana paling menguntungkan?

Run:
    python python/09_groupby_analysis.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from utils import load_clean_data, print_section, format_idr


def groupby_category(df: pd.DataFrame) -> pd.DataFrame:
    """Mean total_sales dan quantity per category."""
    result = (
        df.groupby("category")[["total_sales", "quantity"]]
        .mean()
        .round(2)
        .sort_values("total_sales", ascending=False)
    )
    result.columns = ["avg_total_sales", "avg_quantity"]
    return result


def groupby_kota(df: pd.DataFrame) -> pd.DataFrame:
    """Mean total_sales dan quantity per kota."""
    result = (
        df.groupby("kota")[["total_sales", "quantity"]]
        .mean()
        .round(2)
        .sort_values("total_sales", ascending=False)
    )
    result.columns = ["avg_total_sales", "avg_quantity"]
    return result


def groupby_category_kota(df: pd.DataFrame) -> pd.DataFrame:
    """Mean total_sales dan quantity per kombinasi category + kota."""
    result = (
        df.groupby(["category", "kota"])[["total_sales", "quantity"]]
        .mean()
        .round(2)
        .sort_values("total_sales", ascending=False)
    )
    result.columns = ["avg_total_sales", "avg_quantity"]
    return result


def main():
    print_section("09 · GroupBy Analysis — Category & City")

    df = load_clean_data()

    # ── 1. Per kategori ───────────────────────────────────────────────────────
    print("\n1. RATA-RATA TOTAL_SALES & QUANTITY PER CATEGORY:\n")
    cat_df = groupby_category(df)
    for cat, row in cat_df.iterrows():
        print(f"   {cat:<18}  avg_sales={format_idr(row['avg_total_sales']):<22}  avg_qty={row['avg_quantity']:.2f}")

    top_cat = cat_df.index[0]
    print(f"\n   ★ Kategori paling menguntungkan: {top_cat}")
    print(f"     Rata-rata total_sales = {format_idr(cat_df.loc[top_cat, 'avg_total_sales'])}")

    # ── 2. Per kota ───────────────────────────────────────────────────────────
    print("\n\n2. RATA-RATA TOTAL_SALES & QUANTITY PER KOTA:\n")
    kota_df = groupby_kota(df)
    for kota, row in kota_df.iterrows():
        print(f"   {kota:<22}  avg_sales={format_idr(row['avg_total_sales']):<22}  avg_qty={row['avg_quantity']:.2f}")

    top_kota = kota_df.index[0]
    print(f"\n   ★ Kota paling menguntungkan: {top_kota}")
    print(f"     Rata-rata total_sales = {format_idr(kota_df.loc[top_kota, 'avg_total_sales'])}")

    # ── 3. Per kategori + kota (top 10) ──────────────────────────────────────
    print("\n\n3. TOP 10 KOMBINASI CATEGORY + KOTA (rata-rata total_sales):\n")
    combo_df = groupby_category_kota(df)
    print(combo_df.head(10).to_string())

    top_combo = combo_df.index[0]
    print(f"\n   ★ Kombinasi paling menguntungkan: {top_combo[0]} di {top_combo[1]}")
    print(f"     Rata-rata total_sales = {format_idr(combo_df.iloc[0]['avg_total_sales'])}")
    print(f"     Rata-rata quantity    = {combo_df.iloc[0]['avg_quantity']:.2f}\n")

    return combo_df


if __name__ == "__main__":
    main()
