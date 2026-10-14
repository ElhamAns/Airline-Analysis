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
   - [Bronze Layer — Raw Data](#bronze-layer--raw-data)
   - [Silver Layer — Cleaned Data](#silver-layer--cleaned-data)
   - [Gold Layer — Analytical Data](#gold-layer--analytical-data)
7. [Dashboard & User Interface](#dashboard--user-interface)
8. [Technologies & Tools](#technologies--tools)
9. [Project Structure](#project-structure)
10. [Team](#team)

---

## 📌 Project Overview

The project processes flight movement records associated with King Khalid International Airport and organizes them into data engineering layers for analytical use.

The source Parquet file contains **153,308 records** and **23 columns**, including flight numbers, aircraft and airline information, arrival/departure classifications, airport identifiers, flight statuses, and scheduled timestamps.

The pipeline uses **Databricks notebooks** and **Delta tables** for ingestion, preparation, and analytical modeling. A **Streamlit application** provides the user-facing interface for exploring the data.

## 🎯 Project Goal

Build a structured data pipeline that makes airport flight movement data easier to inspect, prepare, and analyze.

The project objectives are to:

- Preserve the source flight records in a raw data layer.
- Examine missing values, standardize text fields, and identify duplicate records.
- Organize analytical data using a dimensional model.
- Support exploration of flight operations, airports, airlines, and data quality through Streamlit.

## 🗂️ ERD Diagram

The Gold notebook defines a **star schema** with a central flight fact table and dimensions for dates, airlines, airports, aircraft, terminals, and flight statuses.

<img width="1195" height="493" alt="Airline Analysis ERD diagram" src="https://github.com/user-attachments/assets/095ac502-c947-450b-999e-cb26926d70c9" />

## 🏗️ Architecture Diagram

The project organizes source Parquet data through **Bronze**, **Silver**, and **Gold** layers in Databricks, with analytical outputs used by the Streamlit dashboard.

<img width="1684" height="934" alt="Airline Analysis architecture diagram" src="https://github.com/user-attachments/assets/c2c7664b-53c8-4c89-ba01-768826571284" />

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

## 🔄 Medallion Layers

The pipeline uses the **Medallion Architecture** to separate source preservation, data preparation, and analytical modeling.

### 🥉 Bronze Layer — Raw Data

The Bronze notebook reads the source Parquet file and creates a Delta table without applying business-level transformations.

**Table:** `workspace.bronze.flights_raw`

**Source records:** 153,308

The notebook includes row-count checks, schema inspection, a sample preview, and a comparison of the source Parquet and Bronze table counts.

**Notebook:** [`pipelines/bronze/bronze_setup.ipynb`](pipelines/bronze/bronze_setup.ipynb)

### 🥈 Silver Layer — Cleaned Data

The Silver notebook contains data preparation, exploratory quality checks, and deduplication logic. Its transformations include text trimming and empty-string handling, duplicate identification using flight identifiers and scheduled time, and filtering based on airport identifiers and scheduled timestamps.

**Table:** `workspace.silver.flights_clean`

**Recorded Silver row count:** 146,421

The notebook also examines missing values, airline and airport names, flight statuses, and duplicate groups. The recorded checks identified **2,789 extra duplicate rows** under the selected key in Bronze and **4,106 source rows** with missing destination airport codes. These are observations about the source and transformation rules, not claims that all missing values represent invalid flights.

**Notebook:** [`pipelines/silver/silver_setup.ipynb`](pipelines/silver/silver_setup.ipynb)

### 🥇 Gold Layer — Analytical Data

The Gold notebook defines a dimensional model for flight analytics, consisting of a central fact table and six dimensions.

| Table | Role |
|---|---|
| `gold.fact_flights` | Flight records with dimensional references and operational attributes |
| `gold.dim_date` | Calendar attributes derived from scheduled dates |
| `gold.dim_airline` | Airline identifiers and names |
| `gold.dim_airport` | Airport identifiers and names |
| `gold.dim_aircraft` | Aircraft model and registration details |
| `gold.dim_terminal` | Terminal reference values |
| `gold.dim_status` | Flight status reference values |

The Gold notebook also contains analytical SQL for destination rankings, airline flight counts, flight status distribution, scheduled flight hours, and day-of-week patterns, alongside data-model checks.

**Notebook:** [`pipelines/gold/gold_layer.ipynb`](pipelines/gold/gold_layer.ipynb)

## 📈 Dashboard & User Interface

The interactive user interface is built with **Streamlit** and organized into dedicated pages for flight operations, airport insights, airline performance, and data quality.

**[🚀 Open the Airline Analysis Dashboard](https://airline-analysis-9bvjwckaswup245dlhozdk.streamlit.app/)**

The repository contains these dashboard entry points:

| File | Page |
|---|---|
| `streamlit_dashboard/app.py` | Main application |
| `streamlit_dashboard/pages/1_Flight_Operations.py` | Flight Operations |
| `streamlit_dashboard/pages/2_Airport_Insights.py` | Airport Insights |
| `streamlit_dashboard/pages/3_Airline_Performance.py` | Airline Performance |
| `streamlit_dashboard/pages/4_Data_Quality.py` | Data Quality |

Dashboard screenshots are intentionally omitted; the live application is linked directly above.

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
│   │   ├── 1_Flight_Operations.py
│   │   ├── 2_Airport_Insights.py
│   │   ├── 3_Airline_Performance.py
│   │   └── 4_Data_Quality.py
│   ├── app.py
│   └── requirements.txt
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## 👥 Team

Developed collaboratively as part of the **SDA × Le Wagon Data Engineering Bootcamp**.

- **Elham Alansari**
- **Razan Alzahrani**
- **Maryam Mubarak**
- **Nada Almutairi**

<!-- Optional: Replace each team member's name with [Name](their-LinkedIn-profile-URL) when the team chooses to share profile links. -->
