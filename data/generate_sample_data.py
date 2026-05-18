"""
generate_sample_data.py
=======================
Generates a realistic furniture sales dataset (~10,000 rows).
Mimics the structure of a real furniture e-commerce transaction table.

Usage:
    python data/generate_sample_data.py

Output:
    data/furniture_sales.csv
"""

import random
import csv
import os
from datetime import datetime, timedelta

random.seed(42)

NUM_ROWS    = 10_000
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "furniture_sales.csv")

# ── Geography ──────────────────────────────────────────────────────────────────
CITIES = [
    "Jakarta Utara", "Jakarta Pusat", "Jakarta Barat",
    "Jakarta Selatan", "Jakarta Timur", "Bekasi",
    "Depok", "Bogor", "Tangerang Selatan", "Tangerang",
]
CITY_WEIGHTS = [0.13, 0.12, 0.12, 0.12, 0.11, 0.10, 0.09, 0.08, 0.08, 0.05]

# ── Products (category → [(name, price_min, price_max), ...]) ─────────────────
CATEGORIES = {
    "Kamar Tidur": [
        ("Kasur",         2_500_000,  8_000_000),
        ("Lemari Baju",   1_500_000,  5_000_000),
        ("Meja Rias",       750_000,  3_500_000),
        ("Tempat Tidur",  2_000_000,  9_500_000),
        ("Nakas",           300_000,  1_200_000),
    ],
    "Ruang Tamu": [
        ("Sofa",          1_800_000,  8_500_000),
        ("Meja Kopi",       450_000,  2_000_000),
        ("Lemari TV",     1_200_000,  4_500_000),
        ("Rak Buku",        600_000,  2_500_000),
        ("Lemari Hias",     800_000,  3_000_000),
    ],
    "Dapur": [
        ("Kitchen Set",   4_500_000, 15_000_000),
        ("Lemari Dapur",  1_500_000,  5_000_000),
        ("Meja Makan",    1_200_000,  4_500_000),
        ("Kursi Makan",     400_000,  1_800_000),
        ("Bufet",           900_000,  3_500_000),
    ],
    "Ruang Makan": [
        ("Meja Makan",    1_200_000,  6_000_000),
        ("Kursi",           350_000,  1_500_000),
        ("Lemari Makan",    800_000,  3_000_000),
        ("Rak Piring",      250_000,  1_000_000),
    ],
    "Ruang Kerja": [
        ("Meja Kantor",     800_000,  4_000_000),
        ("Kursi Kantor",    600_000,  3_500_000),
        ("Rak Buku",        400_000,  2_000_000),
        ("Lemari Arsip",    700_000,  2_500_000),
    ],
    "Penyimpanan": [
        ("Lemari Sliding", 1_500_000, 6_000_000),
        ("Lemari Sudut",     900_000, 3_500_000),
        ("Rak Sepatu",       250_000, 1_200_000),
        ("Lemari Laci",      700_000, 2_800_000),
    ],
}

STATUS_CHOICES = ["completed", "cancelled"]
STATUS_WEIGHTS = [0.8972, 0.1028]
SHIPPING_FEES  = [40_000, 50_000, 60_000, 75_000]

EXCEL_EPOCH = datetime(1899, 12, 30)
START_DATE  = datetime(2025, 1,  1)
END_DATE    = datetime(2025, 12, 31)


def weighted_choice(items, weights):
    r, cum = random.random(), 0
    for item, w in zip(items, weights):
        cum += w
        if r <= cum:
            return item
    return items[-1]


def random_date():
    return START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days))


def excel_serial(dt):
    return (dt - EXCEL_EPOCH).days


def make_row(n: int) -> dict:
    dt       = random_date()
    kota     = weighted_choice(CITIES, CITY_WEIGHTS)
    category = random.choice(list(CATEGORIES.keys()))
    product_name, price_min, price_max = random.choice(CATEGORIES[category])

    price        = random.randint(price_min // 50_000, price_max // 50_000) * 50_000
    quantity     = random.choices([1, 2, 3, 4], weights=[0.65, 0.25, 0.07, 0.03])[0]
    shipping_fee = random.choice(SHIPPING_FEES)
    total        = price * quantity
    total_sales  = total + shipping_fee
    status       = weighted_choice(STATUS_CHOICES, STATUS_WEIGHTS)

    return {
        "year":             dt.year,
        "month":            dt.month,
        "day":              dt.day,
        "sales_date_std":   excel_serial(dt),
        "order_id":         f"ORD{str(n).zfill(5)}",
        "customer_name":    f"Customer_{random.randint(1, 5000)}",
        "product_name":     product_name,
        "category":         category,
        "price":            price,
        "quantity":         quantity,
        "total":            total,
        "shipping_fee":     shipping_fee,
        "total_sales":      total_sales,
        "status":           status,
        "shipping_address": f"Kelurahan {random.randint(1, 200)} {kota}",
        "kota":             kota,
    }


FIELDNAMES = [
    "year", "month", "day", "sales_date_std",
    "order_id", "customer_name", "product_name", "category",
    "price", "quantity", "total", "shipping_fee", "total_sales",
    "status", "shipping_address", "kota",
]


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for i in range(1, NUM_ROWS + 1):
            writer.writerow(make_row(i))
    print(f"Generated {NUM_ROWS:,} rows  →  {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
