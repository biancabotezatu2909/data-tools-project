# Data Toolkit Project 

**Author:** Bianca-Ioana Botezatu  
**Date:** January 2026

## Project Overview
This project establishes a **reproducible data pipeline** designed for managing and processing **Institutional Records**. The goal is to transform raw institutional data into analysis-ready formats while maintaining a strict audit trail.

## Dataset Description

- **Source:** Course instructor (internal hospital data)
- **Files:** records_2022.csv, records_2023.csv
- **Format:** Tab-separated CSV files
- **Records:** ~[fill in after counting] total records
- **Categories:** Medication administration, Billing transactions
- **Departments:** RAD, WARD_B, ICU, ADMIN
- **Time Coverage:** January 2022 - December 2023

### Known Data Quality Issues
- Date formats are inconsistent (3 different formats)
- Case sensitivity issues in source_system and status fields
- Mixed currency units (SEK, EUR)

---

## Project Structure
The repository is organized to follow data science best practices:

```text
data-toolkit-project/
├── data/
│   ├── raw/          # Original dataset (read-only)
│   ├── interim/      # Intermediate processing steps
│   └── processed/    # Final cleaned datasets
├── src/              # Python/R scripts for processing
├── workflows/        # GitHub Actions or local automation scripts
├── reports/          # Summaries and data visualizations
├── docs/             # Technical documentation & data dictionaries
├── README.md         # Project overview
└── CHANGELOG.md      # Version history & updates
```
## Quick Start

(Instructions will be added next when pipeline is built)

## Data Integrity

File checksums are stored in `docs/checksums.sha256`. Verify integrity before analysis:

**Mac/Linux:**
```bash
shasum -a 256 -c docs/checksums.sha256
```
## Data Privacy & Usage

**IMPORTANT:** This dataset contains sensitive medical and financial information.

**Restrictions:**
- Internal use only
- Do not upload to public repositories
- Do not share outside the organization
- Local storage only
- Use aggregate reporting (no individual records in outputs)

## Documentation

- **Data Dictionary:** `docs/data_dictionary.md` - Column definitions and data types
- **Metadata:** `docs/metadata.yaml` - Dataset provenance and constraints
- **Integrity Notes:** `docs/integrity_notes.md` - File Integrity Verification

## Reproducible Environment

This project uses Python 3.14 (or later recommended) and the dependencies listed in `requirements.txt`.

### Steps to set up the environment

1. **Create a virtual environment**
```bash
python -m venv venv
```

2. **Activate the environment**

-  Windows
```bash
venv\Scripts\activate
```
-  Mac/Linux
```bash
source venv/bin/activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Verify the environment**
```bash
python -c "import pandas as pd; import numpy; import matplotlib"
```
If no errors appear, the environment is ready.

5. **Run the project**
```bash
python src/process_dataset.py
python src/generate_report.py
```