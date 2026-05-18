"""
06_data_type_conversion.py
===========================
Soal 6: Load dataset dengan Pandas, tampilkan df.info().
Identifikasi kolom yang tipe datanya perlu diubah dan jelaskan alasannya.

Run:
    python python/06_data_type_conversion.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from utils import load_data, DATA_PATH, print_section


def main():
    # ── 1. Load data ──────────────────────────────────────────────────────────
    print_section("06 · Data Type Conversion Analysis")
    df = load_data(DATA_PATH)

    # ── 2. Info SEBELUM konversi ───────────────────────────────────────────────
    print("\n>>> INFORMASI DATASET SEBELUM KONVERSI:\n")
    print(df.info())

    # ── 3. Identifikasi kolom yang perlu diubah ────────────────────────────────
    print("""
Kolom yang perlu diubah tipe data:
  ┌────────────────────────────────────────────────────────────────────┐
  │ Kolom           │ Tipe asal  │ Tipe target    │ Alasan             │
  ├────────────────────────────────────────────────────────────────────┤
  │ sales_date_std  │ int64      │ datetime64[ns] │ Serial Excel →     │
  │                 │            │                │ Agar bisa dipakai  │
  │                 │            │                │ untuk analisis     │
  │                 │            │                │ tren & sorting     │
  │                 │            │                │ berdasarkan waktu. │
  └────────────────────────────────────────────────────────────────────┘
""")

    # ── 4. Konversi sales_date_std ─────────────────────────────────────────────
    # Serial number Excel dihitung dari 1899-12-30 (origin Excel)
    df["sales_date_std"] = pd.to_datetime(
        df["sales_date_std"],
        unit="D",
        origin="1899-12-30",
    )

    # ── 5. Info SESUDAH konversi ───────────────────────────────────────────────
    print(">>> INFORMASI DATASET SESUDAH KONVERSI:\n")
    print(df.info())

    # ── 6. Tampilkan sample kolom tanggal setelah konversi ────────────────────
    print("\nSample data sales_date_std setelah konversi:")
    print(df[["order_id", "sales_date_std"]].head(5).to_string(index=False))

    print("\n✅  Kolom sales_date_std berhasil dikonversi ke datetime64[ns].")
    print("    Sekarang bisa digunakan untuk: .dt.month, .dt.year, sorting, dll.\n")

    return df


if __name__ == "__main__":
    main()
