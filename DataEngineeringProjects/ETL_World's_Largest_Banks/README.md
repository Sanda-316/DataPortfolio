# 🏦 Automated ETL Pipeline for Top 10 Largest Banks by Market Capitalization

This project automates the extraction, transformation, and loading of data regarding the top 10 largest banks in the world, ranked by market capitalization (USD). I developed this ETL pipeline as a data engineer for a research organization, focusing on streamlining quarterly financial reporting.

---

## 🧠 Project Overview

As part of my role, I was tasked with building a robust ETL system that:

1. **Extracts** the latest list of the top 10 largest banks by market capitalization (in USD) from a reliable web source.
2. **Transforms** the market capitalization data into GBP, EUR, and INR, using exchange rates provided via a CSV file.
3. **Loads** the processed information into:
   - A local CSV file (`Top10_Banks_MarketCap.csv`)
   - A database table within `Banks_MarketCap.db`
4. **Automates** the entire process so it can be executed each financial quarter, ensuring up-to-date reporting.

---

## ⚙️ Tools & Technologies

- **Python 3**
- **Pandas**
- **Requests** (for web data extraction)
- **CSV**
- **SQLite3** (for database storage)
- **Logging module**

---

## 📂 Files Included

| File                        | Description                                    |
|-----------------------------|------------------------------------------------|
| `etl_banks_marketcap.py`    | Main ETL script for banks data                 |
| `exchange_rates.csv`        | CSV file containing exchange rates             |
| `Top10_Banks_MarketCap.csv` | Processed output table in CSV format           |
| `Banks_MarketCap.db`        | SQLite database storing banks data             |
| `etl_banks_log.txt`         | Execution log file                             |

---

## 🔄 ETL Workflow

```text
Extract (Top 10 Banks by Market Cap in USD)
        ↓
Transform (Convert Market Cap to GBP, EUR, INR using exchange rates)
        ↓
Load (Save as CSV + Store in SQLite DB)
        ↓
Automated Execution (Ready for quarterly reporting)
```

---

## 🧠 Key Learnings

Through this project, I learned how to:

- 🏦 Extract up-to-date financial data from online sources.
- 🔀 Transform monetary values into multiple currencies using current exchange rates.
- 📦 Store and manage data in both CSV and database formats for flexible analysis and reporting.
- 🔄 Build a repeatable, automated ETL pipeline suitable for periodic financial reporting.
- 🧾 Implement logging to ensure transparency and traceability throughout the data workflow.

---
