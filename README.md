# ✈️ Airline Analysis

**Data Engineering Project | SDA × Le Wagon Data Engineering Bootcamp**

Airline Analysis is a data engineering and analytics project focused on flight movements associated with **King Khalid International Airport (RUH / OERK)** in Riyadh, Saudi Arabia. It uses **Databricks**, **Delta Lake**, and a **Bronze–Silver–Gold Medallion Architecture** to organize aviation data for exploration and reporting through an interactive **Streamlit dashboard**.

🔗 **[🖥️ Explore the Interactive Dashboard](https://airline-analysis-9bvjwckaswup245dlhozdk.streamlit.app/)**

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)
2. [Project Goal](#project-goal)
3. [ERD Diagram](#erd-diagram)
4. [Architecture Diagram](#architecture-diagram)
5. [Selected Sources](#selected-sources)
6. [Medallion Layers](#medallion-layers)
   - [Bronze Layer — Preserving the Source](#bronze-layer--preserving-the-source)
   - [Silver Layer — Improving Data Quality](#silver-layer--improving-data-quality)
   - [Gold Layer — Structuring Analytical Data](#gold-layer--structuring-analytical-data)
7. [Dashboard & User Interface](#dashboard--user-interface)
8. [Technologies & Tools](#technologies--tools)
9. [Project Structure](#project-structure)
10. [Team](#team)

---

<a id="project-overview"></a>
## 📌 Project Overview

The project processes flight movement records associated with King Khalid International Airport and organizes them into data engineering layers for analytical use.

The source Parquet file contains **153,308 records** and **23 columns**, including flight numbers, aircraft and airline information, arrival/departure classifications, airport identifiers, flight statuses, and scheduled timestamps.

The pipeline uses **Databricks notebooks** and **Delta tables** for ingestion, preparation, and analytical modeling. A **Streamlit application** provides the user-facing interface for exploring the data.

<a id="project-goal"></a>
## 🎯 Project Goal

Build a structured data pipeline that makes airport flight movement data easier to inspect, prepare, and analyze.

The project objectives are to:

- Preserve the source flight records in a raw data layer.
- Examine missing values, standardize text fields, and identify duplicate records.
- Organize analytical data using a dimensional model.
- Support exploration of flight operations, airports, airlines, and data quality through Streamlit.

<a id="erd-diagram"></a>
## 🗂️ ERD Diagram

The Gold notebook defines a **star schema** with a central flight fact table and dimensions for dates, airlines, airports, aircraft, terminals, and flight statuses.

<img width="1195" height="493" alt="Airline Analysis ERD diagram" src="https://github.com/user-attachments/assets/095ac502-c947-450b-999e-cb26926d70c9" />

<a id="architecture-diagram"></a>
## 🏗️ Architecture Diagram

The project organizes source Parquet data through **Bronze**, **Silver**, and **Gold** layers in Databricks, with analytical outputs used by the Streamlit dashboard.

<img width="1684" height="778" alt="Airline Analysis architecture diagram" src="https://github.com/user-attachments/assets/6c6b5ed1-98d1-4b79-bd1e-8b05febce2fd" />

<a id="selected-sources"></a>
## 📊 Selected Sources

### King Khalid International Airport Flights Dataset

The project uses the [King Khalid International Airport Flights Dataset on Kaggle](https://www.kaggle.com/datasets/mohammedalsubaie/king-khalid-international-airport-flights-dataset/code).

| Property | Description |
|---|---|
| Dataset | King Khalid International Airport Flights |
| Airport | King Khalid International Airport, Riyadh (RUH / OERK) |
| Source file | `flights_RUH.parquet` |
| File format | Apache Parquet |
| Source records | 153,308 |
| Source columns | 23 |

The data contains flight identifiers, aircraft information, airline codes and names, airport information, flight classifications, and scheduled times. The source is stored in the repository under `data/`.

<a id="medallion-layers"></a> 

## 🔄 Medallion Layers

The pipeline follows the **Bronze–Silver–Gold Medallion Architecture** in Databricks, separating raw data preservation, data quality transformations, and analytical modeling into three layers.

<a id="bronze-layer--preserving-the-source"></a>
### 🥉 Bronze Layer — Preserving the Source

**Approach:** Ingest the original Parquet dataset into a Delta table without applying business-level transformations.

**Purpose:** Preserve the original flight records for traceability, inspection, and comparison with downstream layers.

**Output:** `workspace.bronze.flights_raw` — **153,308 records**

**Implementation:** [Bronze Notebook](pipelines/bronze/bronze_setup.ipynb)

---

<a id="silver-layer--improving-data-quality"></a>
### 🥈 Silver Layer — Improving Data Quality

**Approach:** Standardize text fields, handle empty strings, identify and remove duplicate flights, and apply required-field filters for airport identifiers and scheduled timestamps.

**Purpose:** Prepare consistent and structured flight records for downstream analytical processing.

**Output:** `workspace.silver.flights_clean` — **146,421 records**

**Implementation:** [Silver Notebook](pipelines/silver/silver_setup.ipynb)

---

<a id="gold-layer--structuring-analytical-data"></a>
### 🥇 Gold Layer — Structuring Analytical Data

**Approach:** Organize the cleaned flight data into a **star schema** consisting of one central fact table and six dimension tables.

**Purpose:** Structure flight operations data for efficient analytical queries, aggregations, and dashboard reporting.

**Output:**
- **Fact table:** `fact_flights`
- **Dimension tables:** `dim_date`, `dim_airline`, `dim_airport`, `dim_aircraft`, `dim_terminal`, and `dim_status`

**Implementation:** [Gold Notebook](pipelines/gold/gold_layer.ipynb)

<a id="dashboard--user-interface"></a>
## 📈 Dashboard & User Interface

The interactive user interface is built with **Streamlit** and organized into dedicated pages for project overview, flight operations, airport insights, airline performance, and data quality.

🚀 **[Open the Airline Analysis Dashboard](https://airline-analysis-9bvjwckaswup245dlhozdk.streamlit.app/)**

The repository contains these dashboard entry points:

| File | Page |
|---|---|
| `streamlit_dashboard/app.py` | Main application |
| `streamlit_dashboard/pages/Overview.py` | Overview |
| `streamlit_dashboard/pages/Flight_Operations.py` | Flight Operations |
| `streamlit_dashboard/pages/Airport_Insights.py` | Airport Insights |
| `streamlit_dashboard/pages/Airline_Performance.py` | Airline Performance |
| `streamlit_dashboard/pages/4_Data_Quality.py` | Data Quality |

<a id="technologies--tools"></a>
## 🛠️ Technologies & Tools

| Technology | Use in the project |
|---|---|
| Python | Data processing and application code |
| PySpark | DataFrame-based transformations and quality analysis |
| SQL | Data exploration, transformations, dimensional modeling, and analytics |
| Databricks | Notebook-based data engineering environment |
| Delta Lake | Bronze, Silver, and Gold table storage |
| Apache Parquet | Source dataset format |
| Streamlit | Interactive dashboard |
| Git & GitHub | Version control and project repository |

<a id="project-structure"></a>
## 📁 Project Structure

```text
Airline-Analysis/
├── .devcontainer/
│   └── devcontainer.json
├── data/
│   └── flights_RUH.parquet
├── exploration/
├── pipelines/
│   ├── bronze/
│   │   └── bronze_setup.ipynb
│   ├── silver/
│   │   └── silver_setup.ipynb
│   ├── gold/
│   │   └── gold_layer.ipynb
│   └── setup/
│       ├── create_schema.ipynb
│       └── setup_permissions.ipynb
├── src/
│   └── airline_analysis/
│       └── __init__.py
├── streamlit_dashboard/
│   ├── .streamlit/
│   │   └── config.toml
│   ├── pages/
│   │   ├── Overview.py
│   │   ├── Flight_Operations.py
│   │   ├── Airport_Insights.py
│   │   ├── Airline_Performance.py
│   │   └── 4_Data_Quality.py
│   ├── app.py
│   └── requirements.txt
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

<a id="team"></a>
## 👥 Team

Developed collaboratively as part of the **SDA × Le Wagon Data Engineering Bootcamp**.

- **Elham Alansari**
- **Razan Alzahrani**
- **Maryam Mubarak**
- **Nada Almutairi**

<!-- Optional: Replace each team member's name with [Name](their-LinkedIn-profile-URL) when the team chooses to share profile links. -->
