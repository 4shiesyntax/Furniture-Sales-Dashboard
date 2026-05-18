"""
utils.py
========
Helper functions shared across all Python analysis scripts.
"""

import os
import pandas as pd


DATA_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "furniture_sales.csv"
)


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the furniture sales CSV and return a raw DataFrame."""
    df = pd.read_csv(path)
    print(f"Loaded {len(df):,} rows × {df.shape[1]} columns from: {path}")
    return df


def load_clean_data(path: str = DATA_PATH) -> pd.DataFrame:
    """Load the data AND apply the standard cleaning pipeline."""
    df = load_data(path)
    df = convert_date(df)
    df = clean_data(df)
    return df


def convert_date(df: pd.DataFrame) -> pd.DataFrame:
    """Convert sales_date_std (Excel serial int) to datetime column."""
    df = df.copy()
    df["sales_date_std"] = pd.to_datetime(
        df["sales_date_std"], unit="D", origin="1899-12-30"
    )
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicates and rows with any missing values."""
    before = len(df)
    df = df.drop_duplicates()
    df = df.dropna()
    after = len(df)
    if before != after:
        print(f"Cleaned: {before - after:,} rows removed ({before:,} → {after:,})")
    return df


def format_idr(value: float) -> str:
    """Format a number as Indonesian Rupiah string."""
    return f"Rp{value:,.0f}"


def print_section(title: str) -> None:
    width = 68
    print(f"\n{'='*width}")
    print(f"  {title}")
    print(f"{'='*width}")
