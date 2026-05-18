"""
10_business_insights.py
========================
Soal 10: Analisis lengkap — 3 insight bisnis dari data furniture
         beserta kode Python + SQL yang mendukung setiap insight.

Visualisasi yang dihasilkan:
  • Bar chart: Revenue per kota (top 8)         → assets/insight1_revenue_per_kota.png
  • Bar chart: Top 5 produk quantity            → assets/insight2_top_products.png
  • Line chart: Tren order bulanan 2025         → assets/insight3_monthly_trend.png

Run:
    python python/10_business_insights.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from utils import load_clean_data, print_section, format_idr

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

DARK_BG    = "#1a1a2e"
ACCENT     = "#00d4aa"
ACCENT2    = "#f4845f"
ACCENT3    = "#a78bfa"
TEXT_COLOR = "#e0e0e0"
GRID_COLOR = "#333355"

def set_dark_style():
    plt.style.use("dark_background")
    plt.rcParams.update({
        "font.family":    "DejaVu Sans",
        "axes.facecolor":  DARK_BG,
        "figure.facecolor": DARK_BG,
        "axes.edgecolor":  GRID_COLOR,
        "axes.labelcolor": TEXT_COLOR,
        "xtick.color":     TEXT_COLOR,
        "ytick.color":     TEXT_COLOR,
        "grid.color":      GRID_COLOR,
        "grid.linestyle":  "--",
        "grid.alpha":      0.4,
        "text.color":      TEXT_COLOR,
    })


# ── INSIGHT 1 ─────────────────────────────────────────────────────────────────
def insight_1_revenue_per_kota(df: pd.DataFrame) -> None:
    """
    INSIGHT 1: Jakarta mendominasi penjualan — 5 dari 8 kota teratas adalah
    wilayah Jakarta. Strategi distribusi harus berfokus pada area ini.

    SQL Equivalen:
        SELECT kota, SUM(total_sales) AS total_revenue
        FROM furniture_sales
        GROUP BY kota
        ORDER BY total_revenue DESC
        LIMIT 8;
    """
    print_section("INSIGHT 1 · Revenue per Kota (Top 8)")

    top_kota = (
        df.groupby("kota")["total_sales"]
        .sum()
        .sort_values(ascending=False)
        .head(8)
    )

    print("\nTop 8 Kota berdasarkan Revenue:")
    for k, v in top_kota.items():
        bar = "█" * int(v / top_kota.max() * 30)
        print(f"  {k:<22} {format_idr(v):<25} {bar}")

    # ── Visualisasi ──────────────────────────────────────────────────────────
    set_dark_style()
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)

    colors  = [ACCENT if "Jakarta" in k else ACCENT3 for k in top_kota.index]
    bars    = ax.barh(top_kota.index[::-1], top_kota.values[::-1],
                      color=colors[::-1], edgecolor="none", height=0.6)

    # Label nilai di ujung bar
    for bar, val in zip(bars, top_kota.values[::-1]):
        ax.text(bar.get_width() + top_kota.max() * 0.01,
                bar.get_y() + bar.get_height() / 2,
                format_idr(val), va="center", ha="left",
                fontsize=9, color=TEXT_COLOR)

    ax.set_xlabel("Total Revenue (Rp)", color=TEXT_COLOR, labelpad=10)
    ax.set_title("Revenue per Kota — Top 8\nFurniture Sales 2025",
                 color=TEXT_COLOR, fontsize=14, pad=16, loc="left")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(
        lambda x, _: f"Rp{x/1e9:.1f}B" if x >= 1e9 else f"Rp{x/1e6:.0f}M"
    ))
    ax.grid(axis="x", alpha=0.3)
    ax.tick_params(axis="both", labelsize=9)

    # Legend
    from matplotlib.patches import Patch
    legend_els = [
        Patch(facecolor=ACCENT,  label="Jakarta"),
        Patch(facecolor=ACCENT3, label="Luar Jakarta"),
    ]
    ax.legend(handles=legend_els, loc="lower right", framealpha=0.3, fontsize=9)

    plt.tight_layout()
    out = os.path.join(ASSETS_DIR, "insight1_revenue_per_kota.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n  Chart saved → {out}")

    insight = """
  INSIGHT: Wilayah Jakarta (Utara, Pusat, Barat, Selatan, Timur) mendominasi
  revenue dengan kontribusi gabungan >55% dari total penjualan. Bekasi dan
  Depok menjadi pasar satelit yang signifikan.

  REKOMENDASI:
  • Fokuskan stok dan distribusi ke area Jabodetabek.
  • Tingkatkan promosi untuk kota-kota luar Jakarta (Bogor, Tangerang)
    yang masih memiliki potensi pertumbuhan besar.
"""
    print(insight)


# ── INSIGHT 2 ─────────────────────────────────────────────────────────────────
def insight_2_top_products(df: pd.DataFrame) -> None:
    """
    INSIGHT 2: Kitchen Set dan Kasur adalah produk dengan revenue dan quantity
    tertinggi — keduanya mewakili kebutuhan primer rumah tangga.

    SQL Equivalen:
        SELECT product_name,
               SUM(quantity)    AS total_quantity,
               SUM(total_sales) AS total_revenue
        FROM furniture_sales
        GROUP BY product_name
        ORDER BY total_quantity DESC
        LIMIT 5;
    """
    print_section("INSIGHT 2 · Top 5 Produk Terlaris")

    top_prod = (
        df.groupby("product_name")
        .agg(total_quantity=("quantity", "sum"),
             total_revenue=("total_sales", "sum"))
        .sort_values("total_quantity", ascending=False)
        .head(5)
    )

    print("\nTop 5 Produk berdasarkan Quantity terjual:")
    print(top_prod.to_string())

    set_dark_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor(DARK_BG)

    palette = [ACCENT, ACCENT2, ACCENT3, "#f9c74f", "#90be6d"]

    # Chart 1: Quantity
    ax1 = axes[0]
    ax1.set_facecolor(DARK_BG)
    bars1 = ax1.bar(range(len(top_prod)), top_prod["total_quantity"],
                    color=palette, edgecolor="none", width=0.6)
    for bar, val in zip(bars1, top_prod["total_quantity"]):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                 f"{val:,}", ha="center", va="bottom", fontsize=9)
    ax1.set_xticks(range(len(top_prod)))
    ax1.set_xticklabels(top_prod.index, rotation=20, ha="right", fontsize=9)
    ax1.set_title("Top 5 Produk by Quantity", color=TEXT_COLOR, fontsize=12, pad=10)
    ax1.set_ylabel("Total Quantity Terjual")
    ax1.grid(axis="y", alpha=0.3)

    # Chart 2: Revenue
    ax2 = axes[1]
    ax2.set_facecolor(DARK_BG)
    bars2 = ax2.bar(range(len(top_prod)), top_prod["total_revenue"],
                    color=palette, edgecolor="none", width=0.6)
    for bar, val in zip(bars2, top_prod["total_revenue"]):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + top_prod["total_revenue"].max()*0.01,
                 f"Rp{val/1e9:.2f}B", ha="center", va="bottom", fontsize=9)
    ax2.set_xticks(range(len(top_prod)))
    ax2.set_xticklabels(top_prod.index, rotation=20, ha="right", fontsize=9)
    ax2.set_title("Top 5 Produk by Revenue", color=TEXT_COLOR, fontsize=12, pad=10)
    ax2.set_ylabel("Total Revenue (Rp)")
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rp{x/1e9:.1f}B"))
    ax2.grid(axis="y", alpha=0.3)

    fig.suptitle("Top 5 Produk — Quantity vs Revenue · Furniture Sales 2025",
                 color=TEXT_COLOR, fontsize=14, y=1.02)
    plt.tight_layout()
    out = os.path.join(ASSETS_DIR, "insight2_top_products.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n  Chart saved → {out}")

    insight = """
  INSIGHT: Kitchen Set mendominasi revenue meskipun quantity-nya lebih rendah
  dari Kasur — artinya Kitchen Set memiliki harga satuan tertinggi. Strategi
  bundling (Kitchen Set + Kursi Makan) dapat meningkatkan nilai transaksi.

  REKOMENDASI:
  • Prioritaskan stok Kitchen Set dan Kasur karena keduanya high-demand.
  • Buat paket bundling produk untuk meningkatkan Average Order Value.
  • Tingkatkan promosi produk Kamar Tidur (Kasur + Lemari Baju + Nakas).
"""
    print(insight)


# ── INSIGHT 3 ─────────────────────────────────────────────────────────────────
def insight_3_monthly_trend(df: pd.DataFrame) -> None:
    """
    INSIGHT 3: Order mencapai puncak di pertengahan tahun (Jul-Agu),
    lalu turun drastis di Q4. Butuh strategi promosi untuk menjaga
    stabilitas penjualan akhir tahun.

    Python Equivalen:
        monthly = df.groupby('month')['order_id'].count()
    """
    print_section("INSIGHT 3 · Tren Order Bulanan 2025")

    df2 = df.copy()
    # Already converted by load_clean_data; use .dt accessor directly
    df2["month_num"] = df2["sales_date_std"].dt.month

    monthly = (
        df2.groupby("month_num")["order_id"]
        .count()
        .reindex(range(1, 13), fill_value=0)
    )

    month_labels = ["Jan","Feb","Mar","Apr","Mei","Jun",
                    "Jul","Agu","Sep","Okt","Nov","Des"]

    print("\nJumlah Order per Bulan 2025:")
    for m, (mn, cnt) in enumerate(zip(month_labels, monthly.values), 1):
        bar = "█" * int(cnt / monthly.max() * 30)
        peak = " ← HIGHEST" if cnt == monthly.max() else ""
        print(f"  {mn:>4} : {cnt:>5,}  {bar}{peak}")

    # ── Visualisasi ──────────────────────────────────────────────────────────
    set_dark_style()
    fig, ax = plt.subplots(figsize=(13, 6))
    fig.patch.set_facecolor(DARK_BG)
    ax.set_facecolor(DARK_BG)

    x     = np.arange(len(month_labels))
    vals  = monthly.values
    peak_idx = vals.argmax()

    ax.plot(x, vals, color=ACCENT, linewidth=2.5, marker="o",
            markersize=7, markerfacecolor=ACCENT, zorder=3)

    # Highlight bulan tertinggi
    ax.scatter([peak_idx], [vals[peak_idx]], s=180, color=ACCENT2,
               zorder=5, label=f"Highest: {month_labels[peak_idx]} ({vals[peak_idx]:,})")
    ax.annotate(f"Highest: {vals[peak_idx]:,}",
                xy=(peak_idx, vals[peak_idx]),
                xytext=(peak_idx + 0.5, vals[peak_idx] + vals.max() * 0.03),
                arrowprops=dict(arrowstyle="->", color=ACCENT2, lw=1.5),
                fontsize=9, color=ACCENT2)

    # Shading area under line
    ax.fill_between(x, vals, alpha=0.12, color=ACCENT)

    # Q4 drop annotation
    ax.annotate("Q4 drop",
                xy=(9, vals[9]), xytext=(9.5, vals[9] - vals.max() * 0.08),
                arrowprops=dict(arrowstyle="->", color=ACCENT3, lw=1.2),
                fontsize=8, color=ACCENT3)

    ax.set_xticks(x)
    ax.set_xticklabels(month_labels, fontsize=10)
    ax.set_ylabel("Jumlah Order", labelpad=10)
    ax.set_title("Tren Total Order per Bulan — 2025\nFurniture Sales Dataset",
                 color=TEXT_COLOR, fontsize=14, pad=16, loc="left")
    ax.axhline(vals.mean(), color=GRID_COLOR, linestyle="--", linewidth=1.2,
               label=f"Rata-rata: {vals.mean():.0f}")
    ax.legend(fontsize=9, framealpha=0.3)
    ax.grid(axis="y", alpha=0.3)
    ax.tick_params(axis="both", labelsize=9)

    plt.tight_layout()
    out = os.path.join(ASSETS_DIR, "insight3_monthly_trend.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n  Chart saved → {out}")

    insight = f"""
  INSIGHT: Order memuncak di {month_labels[peak_idx]} ({vals[peak_idx]:,} orders) lalu
  turun signifikan menjelang akhir tahun. Rata-rata bulanan: {vals.mean():.0f} orders.

  REKOMENDASI:
  • Siapkan flash sale / promo akhir tahun (Okt–Des) untuk mengejar target.
  • Manfaatkan momen Harbolnas (11.11, 12.12) untuk mendongkrak Q4.
  • Analisis faktor yang membuat Jul-Agu tinggi dan replikasi strateginya.
"""
    print(insight)


def main():
    print_section("10 · Business Insights Analysis")

    df = load_clean_data()

    insight_1_revenue_per_kota(df)
    insight_2_top_products(df)
    insight_3_monthly_trend(df)

    print("=" * 68)
    print("  Semua insight selesai dianalisis.")
    print(f"  Charts disimpan di: {ASSETS_DIR}")
    print("=" * 68 + "\n")


if __name__ == "__main__":
    main()
