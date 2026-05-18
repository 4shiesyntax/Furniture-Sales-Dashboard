-- =============================================================================
-- Query 05: Top 5 Produk dengan Quantity Terjual Terbanyak
-- =============================================================================
-- Tujuan   : Menampilkan 5 produk teratas berdasarkan total quantity terjual.
-- Platform : Google BigQuery (Standard SQL)
-- =============================================================================

SELECT
    product_name,
    SUM(quantity)           AS total_quantity,
    SUM(total_sales)        AS total_revenue,
    COUNT(order_id)         AS total_order,
    ROUND(AVG(price), 0)    AS avg_price,
    ROUND(
        SUM(quantity) * 100.0
        / SUM(SUM(quantity)) OVER (),
        2
    )                       AS quantity_pct
FROM
    `project.dataset.furniture_sales`
GROUP BY
    product_name
ORDER BY
    total_quantity DESC
LIMIT 5;

-- =============================================================================
-- Bonus: Top 5 per kategori (RANK analytic function)
-- =============================================================================

WITH ranked AS (
    SELECT
        category,
        product_name,
        SUM(quantity)       AS total_quantity,
        SUM(total_sales)    AS total_revenue,
        RANK() OVER (
            PARTITION BY category
            ORDER BY SUM(quantity) DESC
        ) AS rnk
    FROM
        `project.dataset.furniture_sales`
    GROUP BY
        category,
        product_name
)
SELECT
    category,
    product_name,
    total_quantity,
    total_revenue,
    rnk
FROM
    ranked
WHERE
    rnk = 1
ORDER BY
    total_quantity DESC;
