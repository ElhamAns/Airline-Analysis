# ✈️ Airline Analysis

**Data Engineering Project | SDA × Le Wagon Data Engineering Bootcamp**

A flight-data engineering and analytics project focused on King Khalid International Airport (RUH / OERK), Riyadh, Saudi Arabia. The project uses **Databricks**, **Delta Lake**, and a **Bronze–Silver–Gold Medallion Architecture** to organize flight movement records for analysis. An interactive **Streamlit dashboard** is planned to present the analytical results.

## 📑 Table of Contents

1. [Project Overview](#-project-overview)
2. [Project Goal](#-project-goal)
3. [ERD Diagram](#-erd-diagram)
4. [Architecture Diagram](#-architecture-diagram)
5. [Selected Sources](#-selected-sources)
6. [Medallion Layers](#-medallion-layers)
   - [Bronze Layer — Raw Data](#-bronze-layer--raw-data)
   - [Silver Layer — Cleaned Data](#-silver-layer--cleaned-data)
   - [Gold Layer — Analytical Data](#-gold-layer--analytical-data)
7. [Dashboard & User Interface](#-dashboard--user-interface)
8. [Technologies & Tools](#-technologies--tools)
9. [Project Structure](#-project-structure)
10. [Project Status](#-project-status)
11. [Team](#-team)

---

## 📌 Project Overview

**Airline Analysis** processes flight movement data associated with **King Khalid International Airport (RUH)**. The source Parquet dataset contains **153,308 records and 23 columns**, including flight identifiers, airlines, aircraft, flight types, statuses, airport details, and scheduled times.

The pipeline uses the Medallion Architecture in Databricks:

**Source Parquet → Bronze (raw) → Silver (cleaned) → Gold (analytical model) → Streamlit (dashboard, planned)**

The Bronze and Silver tables have been implemented. The Gold notebook defines a star schema and analytical queries; its final validation is ongoing.

## 🎯 Project Goal

Build a structured data pipeline that prepares flight movement records for reliable analysis and reporting.

**Objectives:**

- Ingest the original flight dataset into a Delta table.
- Inspect data quality, missing values, and duplicate records.
- Prepare a cleaned Silver dataset for downstream transformations.
- Model analytical data using a Gold-layer fact table and dimensions.
- Present flight-related insights in an interactive **Streamlit dashboard**.

## 🗂️ ERD Diagram

The Gold notebook defines a star-schema-style analytical model centered on `fact_flights`, with date, airline, airport, aircraft, terminal, and status dimensions.

<!-- ERD IMAGE: Replace the src below if you upload an updated ERD. -->
<p align="center">
  <img src="https://github.com/user-attachments/assets/e40ac296-8cf1-4d18-9784-d28ab2af3d97" alt="Airline Analysis ERD diagram" width="100%" />
</p>

> **Diagram note:** Confirm that the image reflects the final Gold schema before treating it as the definitive ERD.

## 🏗️ Architecture Diagram

The project uses Databricks to load Parquet data into Delta tables organized into Bronze, Silver, and Gold layers. The planned presentation layer is Streamlit.

<!-- ARCHITECTURE IMAGE: Replace the src below if you upload an updated architecture diagram. -->
<p align="center">
  <img src="https://github.com/user-attachments/assets/afb4c976-5134-4af9-accb-9eb348200b5d" alt="Airline Analysis pipeline architecture diagram" width="100%" />
</p>

## 📊 Selected Sources

### King Khalid International Airport Flights Dataset

The source is a Parquet file containing flight movement data associated with King Khalid International Airport, Riyadh. The dataset description provided for the project indicates that it was assembled from multiple aviation/flight-tracking APIs.

| Property | Value |
|---|---|
| Source file | `flights_RUH.parquet` |
| Format | Apache Parquet |
| Records | 153,308 |
| Columns | 23 |
| Airport | King Khalid International Airport (RUH / OERK) |
| Original dataset link | **To be added — source URL not yet confirmed** |
| License | **To be verified against the original dataset page** |

The dataset includes `flight_number`, `flight_type`, `status`, airline and aircraft fields, airport identifiers, and scheduled UTC/local times.

## 🔄 Medallion Layers

### 🥉 Bronze Layer — Raw Data

**Purpose:** Preserve the source records in a Delta table for downstream processing.

**Implemented work:**

- Read the source Parquet file from a Databricks Volume.
- Created the Bronze Delta table using SQL.
- Inspected the schema and sample records.
- Compared source and Bronze record counts.
- Inspected Delta table metadata.

**Table:** `workspace.bronze.flights_raw`  
**Verified records:** **153,308**

### 🥈 Silver Layer — Cleaned Data

**Purpose:** Prepare records for analysis through cleaning, deduplication, and data-quality investigation.

**Implemented work:**

- Investigated missing values, flight identifiers, airport codes, airline names, and timestamps.
- Included an initial PySpark step to trim string fields and convert empty strings to nulls.
- Applied deduplication using flight number, scheduled UTC time, origin ICAO, and destination ICAO.
- Applied additional filtering rules.
- Checked for duplicate groups and reconciled Bronze-to-Silver record counts.

**Table:** `workspace.silver.flights_clean`  
**Last verified records:** **146,421**

| Validation finding | Records |
|---|---:|
| Extra duplicate records under the selected flight key in Bronze | 2,789 |
| Bronze records with missing destination airport codes | 4,106 |
| Overlap between extra duplicate rows and missing-code rows | 8 |

No duplicate groups remained in the verified Silver table under the selected key.

> **Review note:** The Silver notebook contains multiple overwrite operations. Its final transformations, including how missing destination codes are handled, are under review. The initial whitespace-cleaning step should not be assumed to survive subsequent table recreation.

### 🥇 Gold Layer — Analytical Data

**Purpose:** Organize cleaned flight records into a star-schema-style model for reporting and dashboard queries.

The uploaded Gold notebook defines these tables:

| Table | Role |
|---|---|
| `gold.fact_flights` | Flight records and references to dimensions |
| `gold.dim_date` | Scheduled date attributes |
| `gold.dim_airline` | Airline details |
| `gold.dim_airport` | Airport details; referenced for origin and destination |
| `gold.dim_aircraft` | Aircraft details |
| `gold.dim_terminal` | Terminal values |
| `gold.dim_status` | Flight status values |

The notebook also contains analytical SQL for destination rankings, airline flight share, flight counts by hour and weekday, status distributions, and missing-dimension reporting.

**Status:** Gold implementation has been written; final data-quality and join validation is still pending. These queries should not yet be presented as verified dashboard outputs.

## 📈 Dashboard & User Interface

An interactive dashboard will be developed using **[Streamlit](https://streamlit.io/)** to present insights derived from the Gold layer.

**Status:** Planned / under development. The final charts, filters, deployment URL, and screenshots will be added after implementation.

<!-- DASHBOARD SCREENSHOT: When ready, insert your screenshot here, for example:
![Streamlit dashboard overview](docs/images/dashboard-overview.png)
-->

## 🛠️ Technologies & Tools

| Technology | Role in this project |
|---|---|
| Python / PySpark | Data cleaning and inspection in Databricks notebooks |
| SQL | Ingestion, validation, modeling, and analytical queries |
| Databricks | Pipeline development and data processing |
| Delta Lake | Bronze, Silver, and Gold table storage |
| Apache Parquet | Original source file format |
| Git & GitHub | Version control and project documentation |
| Streamlit | Planned dashboard and user interface |

## 📁 Project Structure

The exact GitHub directory structure has **not yet been confirmed**. The following notebook filenames have been provided for review; their final repository paths will be documented after confirmation:

- `bronze_setup.py` — Raw ingestion and Bronze checks.
- `silver_setup.py` — Silver cleaning, exploration, deduplication, and validation.
- `gold_layer.py` — Gold dimensions, fact table, and analytical queries.

<!-- Replace this section with the actual GitHub folder tree after confirming it. -->

## 🚧 Project Status

| Component | Status |
|---|---|
| Source data ingestion | Implemented and record count checked |
| Bronze layer | Implemented |
| Silver layer | Implemented; transformation review pending |
| Gold layer | Notebook written; final validation pending |
| Streamlit dashboard | Planned / under development |
| Repository documentation | In progress |

## 👥 Team

Developed collaboratively as part of the **SDA × Le Wagon Data Engineering Bootcamp**.

- **Maryam Mubarak**
- **Razan Alzahrani**
- **Elham Alansari**
- **Nada Almutairi**
