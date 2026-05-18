# 🪑 Furniture Sales Analysis

Mini case study untuk analisis data penjualan furniture menggunakan SQL, Python, Pandas, dan Looker Studio.

## 📌 Project Overview

Project ini dibuat untuk mengeksplorasi proses analisis data end-to-end, mulai dari data cleaning, query SQL, analisis bisnis, sampai visualisasi dashboard.

Tools yang digunakan:

* SQL (BigQuery)
* Python
* Pandas
* Matplotlib
* Looker Studio

Dataset yang digunakan merupakan data sintetis untuk kebutuhan pembelajaran dan portfolio.

---

## 📂 Project Structure

```bash
furniture-sales-analysis/
├── README.md
├── LICENSE
├── .gitignore
├── run_all.py
│
├── data/
│   ├── generate_sample_data.py
│   └── furniture_sales.csv
│
├── sql/
│   ├── 01_dataset_exploration.sql
│   ├── 02_unique_city_analysis.sql
│   ├── 03_completed_orders_jakarta_pusat.sql
│   ├── 04_revenue_by_category.sql
│   └── 05_top_products_quantity.sql
│
├── python/
│   ├── requirements.txt
│   ├── utils.py
│   ├── 06_data_type_conversion.py
│   ├── 07_missing_values_duplicates.py
│   ├── 08_revenue_tier_classification.py
│   ├── 09_groupby_analysis.py
│   └── 10_business_insights.py
│
└── assets/
    ├── insight1_revenue_per_kota.png
    ├── insight2_top_products.png
    └── insight3_monthly_trend.png
```

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/username/furniture-sales-analysis.git
cd furniture-sales-analysis
```

### 2. Install Dependencies

```bash
pip install -r python/requirements.txt
```

### 3. Generate Sample Dataset

```bash
python data/generate_sample_data.py
```

### 4. Run All Analysis

```bash
python run_all.py
```

Atau jalankan file satu per satu:

```bash
python python/06_data_type_conversion.py
python python/07_missing_values_duplicates.py
python python/08_revenue_tier_classification.py
python python/09_groupby_analysis.py
python python/10_business_insights.py
```

---

## 📊 Dataset Schema

| Column           | Description              |
| ---------------- | ------------------------ |
| year             | Tahun transaksi          |
| month            | Bulan transaksi          |
| day              | Tanggal transaksi        |
| sales_date_std   | Format serial Excel date |
| order_id         | ID unik order            |
| customer_name    | Nama customer            |
| product_name     | Nama produk furniture    |
| category         | Kategori produk          |
| price            | Harga produk             |
| quantity         | Jumlah pembelian         |
| total            | Total harga              |
| shipping_fee     | Biaya pengiriman         |
| total_sales      | Total transaksi akhir    |
| status           | Status order             |
| shipping_address | Alamat pengiriman        |
| kota             | Kota tujuan              |

---

## 🧠 SQL Analysis

| No | Analysis                            |
| -- | ----------------------------------- |
| 1  | Dataset exploration                 |
| 2  | Unique city analysis                |
| 3  | Completed orders from Jakarta Pusat |
| 4  | Revenue by category                 |
| 5  | Top selling products                |

---

## 🐍 Python Analysis

| No | Analysis                             |
| -- | ------------------------------------ |
| 6  | Data type conversion                 |
| 7  | Missing values & duplicates handling |
| 8  | Revenue tier classification          |
| 9  | GroupBy analysis                     |
| 10 | Business insights & visualization    |

---

## 💡 Key Insights

### Revenue Tertinggi Berasal dari Area Jakarta

Sebagian besar revenue berasal dari wilayah Jakarta dan kota penyangga seperti Bekasi serta Depok.

### Kitchen Set Memiliki Revenue Paling Besar

Kitchen Set menghasilkan total revenue tertinggi karena memiliki average selling price yang tinggi.

### Penjualan Meningkat di Pertengahan Tahun

Aktivitas transaksi meningkat pada pertengahan tahun dan mulai menurun menjelang akhir tahun.

---

## 📈 Dashboard Features

Dashboard dibuat menggunakan Looker Studio dengan beberapa komponen utama:

* Total Revenue
* Total Orders
* Average Order Value
* Completion Rate
* Revenue by City
* Monthly Sales Trend
* Product Performance Table
* Interactive Filters

---

## ⚙️ Requirements

```txt
Python 3.9+
pandas
numpy
matplotlib
seaborn
```

---

## 👤 Author

**Dika Yugi Pratama**

* GitHub: [https://github.com/4shiesyntax](https://github.com/4shiesyntax)
* Portfolio: [https://lincode.dev](https://lincode.dev)

---

✨ Use your own personal data here. Only
