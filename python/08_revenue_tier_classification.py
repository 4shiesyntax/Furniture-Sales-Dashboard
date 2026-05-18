"""
08_revenue_tier_classification.py
===================================
Soal 8: Buat kolom baru revenue_tier menggunakan pd.cut().
  • Low  : total_sales < 500.000
  • Mid  : total_sales 500.000 – 2.000.000
  • High : total_sales > 2.000.000

Run:
    python python/08_revenue_tier_classification.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from utils import load_clean_data, print_section, format_idr


def create_revenue_tier(df: pd.DataFrame) -> pd.DataFrame:
    """Tambahkan kolom revenue_tier berdasarkan total_sales."""
    df = df.copy()

    bins   = [0, 500_000, 2_000_000, float("inf")]
    labels = ["Low", "Mid", "High"]

    df["revenue_tier"] = pd.cut(
        df["total_sales"],
        bins=bins,
        labels=labels,
        right=True,       # interval: (0, 500k], (500k, 2M], (2M, inf)
        include_lowest=True,
    )

    return df


def main():
    print_section("08 · Revenue Tier Classification")

    df = load_clean_data()
    df = create_revenue_tier(df)

    # ── Sample output ─────────────────────────────────────────────────────────
    print("\nSample data (total_sales + revenue_tier):")
    sample = df[["order_id", "product_name", "total_sales", "revenue_tier"]].head(10)
    print(sample.to_string(index=False))

    # ── Distribusi tier ───────────────────────────────────────────────────────
    print("\n" + "─" * 55)
    print("  DISTRIBUSI REVENUE TIER")
    print("─" * 55)

    tier_summary = (
        df.groupby("revenue_tier", observed=True)
        .agg(
            jumlah_order=("order_id", "count"),
            total_revenue=("total_sales", "sum"),
            avg_total_sales=("total_sales", "mean"),
        )
        .reset_index()
    )
    tier_summary["pct_order"]   = (tier_summary["jumlah_order"] / len(df) * 100).round(2)
    tier_summary["pct_revenue"] = (tier_summary["total_revenue"] / df["total_sales"].sum() * 100).round(2)

    for _, row in tier_summary.iterrows():
        print(f"\n  [{row['revenue_tier']}]")
        print(f"    Jumlah order     : {row['jumlah_order']:,}  ({row['pct_order']:.1f}%)")
        print(f"    Total revenue    : {format_idr(row['total_revenue'])}  ({row['pct_revenue']:.1f}%)")
        print(f"    Rata-rata order  : {format_idr(row['avg_total_sales'])}")

    # ── Tier per kategori ─────────────────────────────────────────────────────
    print("\n" + "─" * 55)
    print("  REVENUE TIER PER KATEGORI")
    print("─" * 55)

    tier_cat = (
        df.groupby(["category", "revenue_tier"], observed=True)["order_id"]
        .count()
        .unstack(fill_value=0)
    )
    print(tier_cat.to_string())

    print("\n✅  Kolom revenue_tier berhasil dibuat.\n")
    return df


if __name__ == "__main__":
    main()
