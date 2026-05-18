-- =============================================================================
-- Query 04: Total Revenue per Kategori Produk
-- =============================================================================
-- Tujuan   : Menghitung total revenue (total_sales) per kategori produk,
--            diurutkan dari yang terbesar.
-- Platform : Google BigQuery (Standard SQL)
-- =============================================================================

SELECT
    category,
    SUM(total_sales)                                    AS total_revenue,
    COUNT(order_id)                                     AS total_order,
    ROUND(AVG(total_sales), 0)                          AS avg_order_value,
    ROUND(
        SUM(total_sales) * 100.0
        / SUM(SUM(total_sales)) OVER (),
        2
    )                                                   AS revenue_pct,
    -- Kumulatif persentase (untuk analisis Pareto)
    ROUND(
        SUM(SUM(total_sales)) OVER (
            ORDER BY SUM(total_sales) DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) * 100.0
        / SUM(SUM(total_sales)) OVER (),
        2
    )                                                   AS cumulative_pct
FROM
    `project.dataset.furniture_sales`
GROUP BY
    category
ORDER BY
    total_revenue DESC;

-- =============================================================================
-- Contoh hasil:
--   1. Kamar Tidur  → revenue tertinggi
--   2. Ruang Tamu
--   3. Dapur
--   4. Ruang Makan
--   5. Ruang Kerja
--   6. Penyimpanan  → revenue terendah
-- =============================================================================
