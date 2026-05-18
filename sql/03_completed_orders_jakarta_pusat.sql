-- =============================================================================
-- Query 03: Filter Order Completed dari Jakarta Pusat
-- =============================================================================
-- Tujuan   : Menampilkan semua order dengan status 'completed' dari
--            kota Jakarta Pusat, diurutkan dari order terbaru.
-- Platform : Google BigQuery (Standard SQL)
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
WHERE
    status = 'completed'
    AND kota  = 'Jakarta Pusat'
ORDER BY
    sales_date_std DESC,   -- terbaru dulu (serial date descending)
    order_id       DESC
LIMIT 50;                  -- hapus LIMIT untuk semua data

-- =============================================================================
-- Catatan:
--   • sales_date_std adalah serial Excel; makin besar = makin baru
--   • Kalau sudah dikonversi ke DATE, ganti ORDER BY sales_date_std
--     dengan ORDER BY PARSE_DATE('%Y%m%d', CAST(sales_date_std AS STRING))
--     atau kolom datetime hasil konversi
-- =============================================================================

-- Versi alternatif — jika sales_date_std sudah dikonversi ke TIMESTAMP:
-- ORDER BY sales_date_timestamp DESC
