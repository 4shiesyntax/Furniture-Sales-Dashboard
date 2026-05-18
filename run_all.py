"""
run_all.py
==========
Script utama untuk menjalankan seluruh pipeline analisis Day 2.
Urutan eksekusi:
  1. Generate sample data
  2. Soal 6  — Data type conversion
  3. Soal 7  — Missing values & duplicates
  4. Soal 8  — Revenue tier classification
  5. Soal 9  — GroupBy analysis
  6. Soal 10 — Business insights + charts

Usage:
    python run_all.py
"""

import subprocess
import sys
import os

ROOT = os.path.dirname(__file__)

STEPS = [
    ("Generate sample data",           ["python", os.path.join(ROOT, "data", "generate_sample_data.py")]),
    ("06 · Data type conversion",     ["python", os.path.join(ROOT, "python", "06_data_type_conversion.py")]),
    ("07 · Missing values & dup",     ["python", os.path.join(ROOT, "python", "07_missing_values_duplicates.py")]),
    ("08 · Revenue tier",             ["python", os.path.join(ROOT, "python", "08_revenue_tier_classification.py")]),
    ("09 · GroupBy analysis",         ["python", os.path.join(ROOT, "python", "09_groupby_analysis.py")]),
    ("10 · Business insights",        ["python", os.path.join(ROOT, "python", "10_business_insights.py")]),
]


def main():
    print("\n" + "=" * 68)
    print("  FURNITURE SALES ANALYSIS — DAY 2 PIPELINE")
    print("=" * 68 + "\n")

    for label, cmd in STEPS:
        print(f"► {label}")
        print("  " + " ".join(cmd[1:]))
        result = subprocess.run(cmd, capture_output=False, text=True)
        if result.returncode != 0:
            print(f"  ✖  Error on step: {label}")
            sys.exit(1)
        print()

    print("=" * 68)
    print("  ✅  Pipeline selesai! Cek folder assets/ untuk charts.")
    print("=" * 68 + "\n")


if __name__ == "__main__":
    main()
