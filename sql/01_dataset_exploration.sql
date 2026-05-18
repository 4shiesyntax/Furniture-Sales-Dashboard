-- =============================================================================
-- Query 01: Dataset Exploration & Column Preview
-- =============================================================================
-- Tujuan   : Menampilkan 10 baris pertama dataset dan melihat semua kolom.
-- Platform : Google BigQuery (Standard SQL)
-- Table    : Ganti `project.dataset.furniture_sales`
--            dengan path tabel BigQuery kamu.
-- =============================================================================

SELECT
    year,
    month,
    day,
    sales_date_std,
    order_id,
    customer_name,
    product_name,
    category,
    price,
    quantity,
    total,
    shipping_fee,
    total_sales,
    status,
    shipping_address,
    kota
FROM
    `project.dataset.furniture_sales`
LIMIT 10;

-- =============================================================================
-- Kolom yang ditemukan:
--   year             → Tahun transaksi (INT)
--   month            → Bulan transaksi (INT)
--   day              → Tanggal hari (INT)
--   sales_date_std   → Serial number Excel untuk tanggal (INT) → perlu dikonversi
--   order_id         → ID unik order (STRING)
--   customer_name    → Nama pelanggan (STRING)
--   product_name     → Nama produk (STRING)
--   category         → Kategori produk (STRING)
--   price            → Harga satuan dalam Rupiah (INT)
--   quantity         → Jumlah unit yang dibeli (INT)
--   total            → price × quantity (INT)
--   shipping_fee     → Biaya pengiriman (INT)
--   total_sales      → total + shipping_fee (INT)
--   status           → Status order: completed / cancelled (STRING)
--   shipping_address → Alamat pengiriman lengkap (STRING)
--   kota             → Kota tujuan pengiriman (STRING)
-- =============================================================================
