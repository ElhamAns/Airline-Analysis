# ✈️ Airline Analysis

**Data Engineering Project | SDA × Le Wagon Data Engineering Bootcamp**

An end-to-end data engineering project focused on processing and analyzing flight movement data from King Khalid International Airport (RUH), Riyadh, Saudi Arabia.

The project uses a **Medallion Architecture (Bronze, Silver, and Gold)** implemented in Databricks to organize raw flight records, improve data quality, and prepare datasets for analysis and visualization through a Streamlit dashboard.

---

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

Airline Analysis is a data engineering project that processes flight movement records associated with King Khalid International Airport (RUH).

The project follows the **Medallion Architecture** to separate raw data ingestion, data cleaning, and analytical transformations.

The dataset contains **153,308 records** covering flight movements, airline information, aircraft details, airport identifiers, flight statuses, and scheduled flight times.

Databricks is used to implement the data pipeline, with Delta tables organized into Bronze, Silver, and Gold layers.

The processed data will be used to support an interactive Streamlit dashboard.

---

## 🎯 Project Goal

The project aims to build a structured data pipeline that transforms raw airport flight records into reliable datasets for analytical reporting.

### Main Objectives

- Ingest and preserve the original flight dataset.
- Apply data cleaning, validation, and deduplication.
- Organize the data using Bronze, Silver, and Gold layers.
- Prepare analytical datasets for flight movement analysis.
- Present the resulting insights through an interactive Streamlit dashboard.

---

## 🗂️ ERD Diagram

<img width="1195" height="493" alt="١" src="https://github.com/user-attachments/assets/e40ac296-8cf1-4d18-9784-d28ab2af3d97" />


<!-- Add the confirmed ERD image here. -->

---

## 🏗️ Architecture Diagram

<img width="1672" height="940" alt="صوره" src="https://github.com/user-attachments/assets/afb4c976-5134-4af9-accb-9eb348200b5d" />

<!-- Add the confirmed architecture diagram here. -->

---

## 📊 Selected Sources

### King Khalid International Airport Flights Dataset

The project uses a flight movement dataset covering arrivals and departures associated with King Khalid International Airport (RUH / OERK), Riyadh, Saudi Arabia.

The dataset was originally collected from multiple aviation and flight-tracking APIs and provided as an Apache Parquet file.

### Dataset Information

| Property | Description |
|---|---|
| **Dataset** | King Khalid International Airport Flights |
| **Source File** | `flights_RUH.parquet` |
| **Format** | Apache Parquet |
| **Records** | 153,308 |
| **Columns** | 23 |
| **Airport** | King Khalid International Airport (RUH / OERK) |
| **License** | Apache 2.0 |

The dataset includes flight numbers, aircraft details, airline identifiers, arrival/departure types, flight statuses, airport information, and scheduled flight timestamps.

**Original Dataset URL:** To be added.

---

## 🔄 Medallion Layers

The data pipeline follows the **Medallion Architecture** to progressively transform flight records from raw source data into analytical datasets.

### 🥉 Bronze Layer — Raw Data

The Bronze layer preserves the original flight records without applying business transformations.

**Implemented Tasks**

- Loaded the source Parquet dataset into Databricks.
- Created a Delta table to store the raw flight records.
- Inspected the table schema and sample records.
- Verified the record count against the original dataset.

**Table:** `workspace.bronze.flights_raw`

**Records:** 153,308

---

### 🥈 Silver Layer — Cleaned Data

The Silver layer prepares the flight data for downstream analysis through data cleaning and quality checks.

**Implemented Tasks**

- Trimmed whitespace and converted empty strings to null values in an initial cleaning step.
- Investigated missing values across dataset columns.
- Analyzed duplicate flight records.
- Applied a deduplication rule based on flight number, scheduled UTC time, and origin/destination airport identifiers.
- Investigated airport codes, airline names, flight statuses, and scheduled timestamps.
- Applied filtering rules to the Silver dataset.
- Validated the resulting record counts and checked for remaining duplicate keys.

**Table:** `workspace.silver.flights_clean`

**Current Records:** 146,421

#### Data-Quality Findings

| Finding | Records |
|---|---:|
| Extra duplicate records identified using the selected flight key | 2,789 |
| Records with missing destination airport codes | 4,106 |
| Records overlapping between the duplicate and missing-code groups | 8 |

Verified that no repeated groups remained under the selected deduplication key.

> **Note:** The Silver cleaning rules are under review, particularly the treatment of records with missing destination airport codes. The current table is being preserved while downstream Gold development continues.

---

### 🥇 Gold Layer — Analytical Data

The Gold layer is intended to transform the cleaned flight records into business-ready datasets for analytical reporting.

**Status:** In progress.

The final Gold tables, metrics, and transformation logic will be documented after implementation and validation.

---

## 📈 Dashboard & User Interface

The project will use **Streamlit** to present flight analysis results through an interactive dashboard.

The dashboard is planned to consume the prepared analytical data from the Gold layer.

**Status:** Planned / under development.

The final dashboard features, charts, filters, and deployment details will be documented once confirmed.

---

## 🛠️ Technologies & Tools

| Technology | Purpose |
|---|---|
| **Python** | Data processing and notebook development |
| **PySpark** | Distributed data transformations |
| **SQL** | Data exploration, validation, and transformations |
| **Databricks** | Data engineering and processing environment |
| **Delta Lake** | Storage format for Medallion tables |
| **Apache Parquet** | Original dataset format |
| **Git & GitHub** | Version control and source code repository |
| **Streamlit** | Planned interactive dashboard |

---

## 📁 Project Structure

The final GitHub repository directory structure will be added after confirmation.

The project includes Databricks notebooks for data ingestion, cleaning, and analytical transformations.

### Confirmed Notebook Files

| File | Description |
|---|---|
| `bronze_setup.py` | Bronze layer setup and validation |
| `silver_setup.py` | Silver layer cleaning, deduplication, and data-quality analysis |

Gold layer and Streamlit dashboard file paths will be added after confirmation.

---

## 🚧 Project Status

| Component | Status |
|---|---|
| Dataset ingestion | Completed |
| Bronze layer | Completed |
| Silver layer | Implemented — under review |
| Gold layer | In progress |
| Streamlit dashboard | Planned / under development |
| Final documentation | In progress |

---

## 👥 Team

......

