# Command Line Dataset Exploration

This document lists simple command-line operations for exploring the hospital records dataset.

---

## Command 1: View First 10 Lines

```bash
head -10 data/raw/records_2023.csv
```

## Command 2: Count Total Records

```bash
wc -l data/raw/records_2023.csv
wc -l data/raw/records_2022.csv
```

## Command 3: Search and Filter Records
Purpose: Find all records containing a specific keyword (e.g., "medication" category) to analyze specific transaction types.

```bash
grep "medication" data/raw/records_2023.csv
```

## Command 4: Count Occurrences of a Value
Purpose: Count how many times a specific value appears (e.g., count all "billing" records vs "medication" records).

```bash
grep -c "billing" data/raw/records_2023.csv
grep -c "medication" data/raw/records_2023.csv
```

## Command 5: Extract Specific Column
Purpose: Extract all values from a specific column (e.g., all departments) to see unique values or analyze distribution.

```bash
cut -d',' -f8 data/processed/records_2023_cleaned.csv | sort | uniq
```

## Command 6: Filter and Save to File
Purpose: Extract high-priority records and save them to a separate file for focused analysis or reporting.

```bash
grep "high" data/raw/records_2023.csv > data/interim/high_priority_records.txt
```

## Command 7: Count Records by Status
Purpose: Analyze how many records are in each status (ok, cancelled, pending, etc.) to identify data quality issues.

```bash
cut -d',' -f7 data/processed/records_combined.csv | sort | uniq -c
```
## Command 8: View Last 10 Records
Purpose: Check the most recent entries in the dataset to verify data completeness and identify the latest date.
```bash
tail -10 data/raw/records_2023.csv
```

