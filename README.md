# Agribusiness Data Analytics – Junior Data Analyst Internship

This repository contains the source code and datasets for the **Junior Data Analyst – Agribusiness Virtual Internship** project.

The workflow follows the methodology described in the internship report: understanding the business problem, data collection/inspection, cleaning, exploratory analysis, visualisation and reporting. The report specifically lists Python (Pandas/NumPy), Matplotlib/Seaborn, spreadsheets, descriptive statistics and correlation as tools/techniques. 

## Student
- **Name:** Rishabh Singh
- **Programme:** B.Tech CSE – AIML
- **Role:** Junior Data Analyst – Agribusiness Virtual Intern
- **Organisation:** YuvaIntern (Henry Harvin Education)
- **Session:** 2026–27

## Repository Structure

```text
agri_analytics_github_repo/
├── data/
│   ├── raw/
│   │   ├── agriculture_market_dataset.csv
│   │   ├── all_india_foodgrain_annual.csv
│   │   └── rice_wheat_comparison.csv
│   └── processed/
├── src/
│   ├── 01_data_understanding.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda_statistics.py
│   ├── 04_outlier_analysis.py
│   ├── 05_correlation_analysis.py
│   ├── 06_visualization.py
│   ├── 07_rice_wheat_comparison.py
│   └── 08_report_insights.py
├── notebooks/
├── outputs/
│   ├── figures/
│   └── tables/
├── docs/
├── requirements.txt
└── README.md
```

## Tasks Covered

1. **Data Understanding** – shape, columns, data types, missing values, duplicates and descriptive statistics.
2. **Data Cleaning** – date parsing, text standardisation, duplicate removal, missing-value treatment, numeric conversion and price consistency checks.
3. **Exploratory Data Analysis** – commodity/state aggregation and summary tables.
4. **Outlier Analysis** – IQR-based outlier detection.
5. **Correlation Analysis** – Pearson correlation between area, production, yield, price and arrivals.
6. **Data Visualisation** – bar chart, line chart, scatter plot and histogram.
7. **Rice vs Wheat Comparison** – comparison of the two crops using the values represented in the internship report.
8. **Insight Generation** – automated summary of key analytical findings.

## Dataset Note

`agriculture_market_dataset.csv` is a **synthetic demonstration dataset** created to make the complete cleaning/EDA workflow reproducible without redistributing a third-party dataset. It contains realistic agricultural fields such as Date, State, District/APMC, Commodity, Area, Production, Yield, Min Price, Modal Price, Max Price and Arrivals.

The Indian Open Government Data platform provides official agriculture datasets, including district/season-wise crop production statistics and mandi price data. For a production or publication-grade project, replace the demo CSV with the downloaded official dataset and preserve its original source metadata.

Official sources:
- Open Government Data – Agriculture sector
- District-wise, season-wise crop production statistics
- Current daily price of various commodities from various markets (Mandi)

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python src/01_data_understanding.py
python src/02_data_cleaning.py
python src/03_eda_statistics.py
python src/04_outlier_analysis.py
python src/05_correlation_analysis.py
python src/06_visualization.py
python src/07_rice_wheat_comparison.py
python src/08_report_insights.py
```

## Expected Outputs

- Cleaned CSV in `data/processed/`
- Summary tables in `outputs/tables/`
- Charts in `outputs/figures/`

## Academic Alignment

The internship report identifies the core modules as:
- Data Understanding and Cleaning
- Exploratory Data Analysis
- Data Visualisation
- Insight Generation and Reporting

This repository implements each module as a separate, easy-to-demonstrate Python task.
