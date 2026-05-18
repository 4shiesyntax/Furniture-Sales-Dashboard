-- =============================================================================
-- Query 02: Total Unique Kota
-- =============================================================================
-- Tujuan   : Menghitung berapa banyak kota unik yang ada di dataset.
-- Platform : Google BigQuery (Standard SQL)
-- =============================================================================

SELECT
    COUNT(DISTINCT kota) AS total_unique_kota
FROM
    `project.dataset.furniture_sales`;

-- =============================================================================
-- Bonus: Tampilkan daftar kota beserta jumlah order per kota
-- =============================================================================

SELECT
    kota,
    COUNT(order_id)          AS total_order,
    SUM(total_sales)         AS total_revenue,
    ROUND(
        SUM(total_sales) * 100.0
        / SUM(SUM(total_sales)) OVER (),
        2
    )                        AS revenue_pct
FROM
    `project.dataset.furniture_sales`
GROUP BY
    kota
ORDER BY
    total_revenue DESC;
