"""
07_missing_values_duplicates.py
================================
Soal 7: Cek missing values dan duplicate rows.
Bersihkan data jika ada. Tampilkan jumlah sebelum dan sesudah.

Run:
    python python/07_missing_values_duplicates.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from utils import load_data, DATA_PATH, print_section


def check_missing_values(df: pd.DataFrame) -> None:
    print("\n" + "─" * 40)
    print("  CEK MISSING VALUES")
    print("─" * 40)
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("  ✅  Tidak ada missing values di semua kolom!")
    else:
        print(f"  ⚠️   Ditemukan missing values:")
        print(missing[missing > 0].to_string())
    print()


def check_duplicates(df: pd.DataFrame) -> int:
    print("─" * 40)
    print("  CEK DUPLICATE ROWS")
    print("─" * 40)
    n_dup = df.duplicated().sum()
    print(f"  Jumlah duplicate rows: {n_dup:,}")
    if n_dup > 0:
        print("  Sample duplikat:")
        print(df[df.duplicated(keep=False)].head(4).to_string(index=True))
    print()
    return n_dup


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("─" * 40)
    print("  PROSES PEMBERSIHAN DATA")
    print("─" * 40)
    before = len(df)

    # Hapus baris duplikat
    df = df.drop_duplicates()
    after_dup = len(df)

    # Hapus baris dengan missing values (jika ada)
    df = df.dropna()
    after_na = len(df)

    print(f"  Jumlah baris SEBELUM dibersihkan : {before:>8,}")
    print(f"  Setelah drop_duplicates          : {after_dup:>8,}  (-{before - after_dup:,})")
    print(f"  Setelah dropna                   : {after_na:>8,}  (-{after_dup - after_na:,})")
    print(f"  ──────────────────────────────────────────")
    print(f"  Total baris dihapus              : {before - after_na:>8,}")
    print(f"  Total baris SESUDAH dibersihkan  : {after_na:>8,}")
    print()
    return df


def main():
    print_section("07 · Missing Values & Duplicate Check")

    df_raw = load_data(DATA_PATH)

    print(f"\n  Dataset shape: {df_raw.shape[0]:,} baris × {df_raw.shape[1]} kolom")

    # ── Cek missing values ────────────────────────────────────────────────────
    check_missing_values(df_raw)

    # ── Cek duplikat ──────────────────────────────────────────────────────────
    n_dup = check_duplicates(df_raw)

    # ── Cleaning ──────────────────────────────────────────────────────────────
    df_clean = clean_data(df_raw)

    # ── Verifikasi akhir ──────────────────────────────────────────────────────
    print("─" * 40)
    print("  VERIFIKASI SETELAH CLEANING")
    print("─" * 40)
    print(f"  Missing values : {df_clean.isnull().sum().sum()}")
    print(f"  Duplikat       : {df_clean.duplicated().sum()}")
    print(f"  Shape final    : {df_clean.shape}")
    print()

    print("  ✅  Data bersih dan siap dianalisis.\n")
    return df_clean


if __name__ == "__main__":
    main()
