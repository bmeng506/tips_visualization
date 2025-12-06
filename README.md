# Restaurant Tipping Analysis Dashboard

This project is a small data visualization workflow built around the classic `tips` dataset from `seaborn`.

It has two main parts:

1. A Python script that loads the data, performs basic transformations, and exports charts as PNG files.  
2. A static Tailwind CSS frontend that displays these charts in an interactive dashboard.

---

## Features

- Uses the built-in `tips` dataset from `seaborn`
- Computes and visualizes:
  - Distribution of tip percentage
  - Tip percentage by day of week
  - Weekday vs weekend tipping
  - Lunch vs dinner tipping
  - Tip percentage vs party size
  - Tip vs total bill (with color and size encodings)
  - Average tip percentage by day and meal
- Python generates all charts as PNGs (no JS charting logic)
- Tailwind-based dashboard provides:
  - View mode filters (All, Overview, Day/Meal, Money/Size)
  - Quick insight chips that scroll to specific charts
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
```

---

## Requirements

### Python side

- Python 3.x  
- `pandas`  
- `seaborn`  
- `matplotlib`

Install with:

```bash
pip install pandas seaborn matplotlib
```

### Frontend side

The frontend is pure HTML/CSS/JS:

- Tailwind CSS via CDN (already included in `index.html`)
- No build step required
- Any modern browser should work

---

## Step 1: Generate Charts with Python

From the project folder:

```bash
cd /path/to/data_proj
python tip_analysis.py
```

The script will:

- Load the `tips` dataset from `seaborn`
- Add a `tip_pct` column
- Create several plots with `seaborn` and `matplotlib`
- Save each chart into the `charts/` folder as a PNG

Make sure the script runs without errors and that the `charts/` directory contains the expected `.png` files.

---

## Step 2: Run the Frontend Locally

Because the HTML uses relative image paths and a separate JS file, it is easiest to use a simple local HTTP server.

From the project folder:

```bash
cd /path/to/data_proj
python -m http.server 8000
```

Then open in a browser:

```text
http://localhost:8000/index.html
```

Features:

- A header describing the project  
- Controls at the top (view mode buttons, question dropdown)  
- A grid of cards, each containing one of the charts  
- The ability to click on chips or questions to scroll to specific charts  
- The ability to click on a chart to view a larger version in a lightbox

---

## How It Works

### Data and Analysis (Python)

The `tip_analysis.py` script:

1. Loads the `tips` dataset via `seaborn.load_dataset("tips")`.  
2. Creates a `tip_pct` field: `tip / total_bill * 100`.  
3. Produces several plots:
   - Histogram of tip percentage
   - Boxplots by day, weekday vs weekend, and lunch vs dinner
   - Scatter plots for tip percentage vs party size, and tip vs total bill
   - A summary bar chart of average tip percentage by day and meal  
4. Saves each figure as a PNG in the `charts/` directory.

You can re-run the script at any time to regenerate or update the charts.

### Frontend and Interactivity (Tailwind + JS)

The HTML dashboard:

- Uses Tailwind CSS utility classes for layout and styling (via CDN).  
- Displays each PNG in a card with:
  - A chart title  
  - A short descriptive subtitle  
  - A collapsible “What this shows” explanation section  
- Uses `app.js` to add interactivity:
  - Filter visible charts by category (overview, time-based, money/size)
  - Scroll to specific charts when insight chips or question options are selected
  - Show a larger version of each chart in a modal lightbox when an image is clicked

No charting libraries are used on the frontend side. All data processing and plotting happens in Python.

---

## Troubleshooting

- If images do not load:
  - Confirm the `charts/` directory exists and contains the PNG files.
  - Confirm the filenames in `index.html` match the actual filenames in `charts/`.
  - Ensure you started the HTTP server from the same folder as `index.html`.

- If the JavaScript interactions do not work:
  - Make sure `app.js` is in the same directory as `index.html`.
  - Confirm that the `<script src="app.js"></script>` tag is present at the bottom of `index.html`.
  - Open the browser console (Developer Tools) to check for errors.

---

## License

You may adapt and reuse this project structure for your own data visualization projects.
