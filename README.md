<img src="https://github.com/Sanda-316/DataPortfolio25/blob/main/Sisanda's%20Dynamic%20Data%20World.png?raw=true" alt="Sisanda's Data Playground Banner" width="100%" style="height:320px; object-fit:cover;">

 # 📊 Sisanda's Data Portfolio

Hi there, welcome to my data portfolio. This repository showcases my skills and work in **Power BI** and **Data Engineering**, including dashboards, ETL pipelines, and data workflows.

---

## 📁 About Me

👩🏾‍💻 Just your friendly neighborhood data enthusiast, crunching numbers and chasing insights!  
I’m all about turning messy data into “aha!” moments. Whether it's slicing cricket stats or decoding panic attack patterns, I live for digging into the data and telling stories with it—charts, dashboards, queries and all. Always learning and forever curious.  
Let’s connect on [LinkedIn](https://www.linkedin.com/in/sisanda-m-sibanda-7a2b941aa) and talk all things data (or cricket, or T-shirts... you’ll see why)! 🏏👕📊

---
<img src="https://github.com/Sanda-316/DataPortfolio25/blob/main/ChatGPT%20Image%20Aug%201%2C%202025%2C%2009_02_40%20PM.png?raw=true" alt="Power BI Projects Banner" width="100%" style="height:320px; object-fit:cover;">

## 🔷 Power BI Data Analyst Projects

## 📊 Power BI Projects

| Project | Preview | Description | Tools & Techniques |
|---------|---------|-------------|--------------------|
| [🏏 **Cricket Analysis**](PowerBIProjects/CricketAnalysis) | ![Cricket Dashboard](PowerBIProjects/CricketAnalysis/screenshots/dashboard-view.png) | Player-level analysis of South Africa vs India matches, covering batting, bowling, and fielding stats. | Power BI, PowerQuery, DAX (`LOOKUPVALUE`, `RANKX`, `POWER`, `ABS`), Web Scraping |
| [🧠 **Panic Attack Insights**](PowerBIProjects/PanicAttackInsights) | ![Panic Dashboard](PowerBIProjects/PanicAttackInsights/screenshots/panic-dashboard.png) | Analysis of panic attack patterns, triggers, and durations, segmented by age group. | Power BI, Snowflake, PowerQuery, DAX (`IF`, `SWITCH`, `COUNTROWS`, `FILTER`, `DIVIDE`) |
| [👕 **Men's T-Shirt Sales Report**](PowerBIProjects/TShirtSalesReport) | ![T-Shirt Dashboard](PowerBIProjects/TShirtSalesReport/screenshots/tshirt-dashboard.png) | Sales and profitability insights for men’s T-shirt brands, including top brands by price and profit %. | Power BI, Azure SQL, PowerQuery, DAX (custom `Discount %`, `Profit %`, `Cost Price`) |

---
## ⚙️ Data Engineering Projects

### 1. Automated GDP ETL Pipeline
**Description**:  
This project automates the extraction, transformation, and loading (ETL) of global GDP data from the International Monetary Fund (IMF) website. The pipeline fetches the latest GDP figures by country, rounds GDP values to two decimal places, and loads the cleaned data into both a JSON file and a SQLite database. It also logs the ETL process and runs a validation query to display countries with GDPs over 100 billion USD.  
**Tools Used**: Python, Pandas, BeautifulSoup4, SQLite3, Logging  
**Code Repository**: [DataPortfolio/DataEngineeringProjects](https://github.com/Sanda-316/DataPortfolio/tree/main/DataEngineeringProjects) 

---

### 2. Automated ETL Pipeline for Top 10 Largest Banks by Market Capitalization
**Description**:  
In this project, I built an automated ETL pipeline for a research organization to compile, transform, and store data on the top 10 largest banks in the world by market capitalization. The pipeline extracts the latest bank rankings (in USD), transforms values into GBP, EUR, and INR using exchange rates from a CSV file, and loads the results into both a CSV and a SQLite database. The system is designed for quarterly automated execution.  
**Tools Used**: Python, Pandas, Requests, SQLite3, Logging  
**Code Repository**: [[DataPortfolio/DataEngineeringProjects](https://github.com/Sanda-316/DataPortfolio/tree/main/DataEngineeringProjects) ](https://github.com/Sanda-316/DataPortfolio/tree/main/DataEngineeringProjects/ETL_World's_Largest_Banks) 




