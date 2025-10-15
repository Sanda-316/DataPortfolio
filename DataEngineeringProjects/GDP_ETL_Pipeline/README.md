# 🌍 Automated GDP ETL Pipeline

This project automates the extraction and transformation of **global GDP data** from the International Monetary Fund (IMF) website and loads it into both a **JSON file** and a **SQLite database**.

---

## 🧠 Project Overview

An international firm expanding its business globally required an automated process to fetch and store GDP data by country.  
As a Junior Data Engineer, I developed a Python-based ETL pipeline that:
1. **Extracts** the latest GDP data from the IMF webpage.
2. **Transforms** the data — rounding GDP values to 2 decimal places.
3. **Loads** the clean data into:
   - A JSON file (`Countries_by_GDP.json`)
   - A database table (`Countries_by_GDP`) inside `World_Economies.db`
4. **Logs** the entire execution process to `etl_project_log.txt`
5. **Runs a validation query** to display countries with GDPs over **100 billion USD**.

---

## ⚙️ Tools & Technologies
- **Python 3**
- **SQLite3**
- **BeautifulSoup4**
- **Requests**
- **Pandas**
- **JSON**
- **Logging module**

---

## 📂 Files Included

| File | Description |
|------|-------------|
| `etl_project_gdp.py` | Main ETL script |
| `World_Economies.db` | SQLite database storing GDP data |
| `etl_project_log.txt` | Execution log file |
| `screenshots/pipeline_overview.png` | Visual overview of the ETL pipeline |

---

## 🔄 ETL Workflow

```text
Extract (IMF Web Data)
        ↓
Transform (Clean, Round GDPs)
        ↓
Load (JSON + SQLite DB)
        ↓
Query & Log (Display GDP > 100B)

---
## 🧠 Key Learnings

Through this project, I learned how to:

🧩 Build a complete ETL pipeline from scratch using Python and automation principles.

🌐 Extract and parse HTML tables from the web using pandas.read_html and BeautifulSoup4.

🧮 Clean and transform data efficiently using Pandas operations and data type conversions.

🗃️ Store structured data in multiple formats — JSON and SQLite — for flexible data use.

🧾 Implement logging to ensure transparency and traceability of data workflows.

💬 Run SQL queries for post-load validation and business insights.

🔁 Automate repetitive data collection for real-world data engineering use cases.
