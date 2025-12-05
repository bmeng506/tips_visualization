# Restaurant Tipping Analysis Dashboard

This project is a small data visualization workflow built around the classic `tips` dataset from `seaborn`.  
It has two main parts:

1. A Python script that loads the data, performs basic transformations, and exports charts as PNG files.
2. A static Tailwind CSS frontend that displays these charts in a simple interactive dashboard.

You can use this as a template for future data → image → web projects.

---

## Features

- Uses the `tips` dataset from `seaborn`
- Computes and visualizes:
  - Distribution of tip percentage
  - Tip percentage by day of week
  - Weekday vs weekend tipping
  - Lunch vs dinner tipping
  - Tip percentage vs party size
  - Tip vs total bill (color and size encodings)
  - Average tip percentage by day and meal
- Python generates all charts (no JS charting logic)
- Tailwind-based dashboard provides:
  - View mode filters (All, Overview, Day/Meal, Money/Size)
  - Quick insight chips to scroll to specific charts
  - Question dropdown to jump to relevant visualizations
  - Click-to-zoom lightbox for each chart image

---

## Project Structure

Approximate folder layout:

```text
data_proj/
├─ tip_analysis.py         # Python script that generates charts
├─ index.html              # Tailwind HTML dashboard
├─ app.js                  # Small JS file for filters, scrolling, and lightbox
└─ charts/                 # Generated chart images (created by Python)
   ├─ tip_pct_distribution.png
   ├─ tip_pct_by_day.png
   ├─ tip_pct_weekday_weekend.png
   ├─ tip_pct_by_meal.png
   ├─ tip_pct_vs_party_size.png
   ├─ tip_vs_total_bill.png
   └─ avg_tip_pct_by_day_meal.png
