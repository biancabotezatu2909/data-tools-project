# src/validate_data.py
import pandas as pd
import os

RAW_DIR = "data/raw"
DATASETS = ["records_2022.csv", "records_2023.csv"]

def validate_dataset(filename):
    filepath = os.path.join(RAW_DIR, filename)
    print(f"Validating {filename}...")

    data = pd.read_csv(filepath)

    # Expected columns by dataset
    expected_cols_2022 = ["record_id", "date", "category", "value", "unit", "source", "status"]
    expected_cols_2023 = ["record_id", "date", "category", "value", "unit", "source_system", "status", "department", "priority"]

    expected_cols = expected_cols_2022 if "2022" in filename else expected_cols_2023

    # Check missing columns
    missing_cols = [col for col in expected_cols if col not in data.columns]
    if missing_cols:
        print(f"WARNING: Missing columns: {missing_cols}")
    else:
        print(f"All expected columns present.")

    # Check for duplicate record_id
    if "record_id" in data.columns:
        duplicate_count = data.duplicated(subset="record_id").sum()
        if duplicate_count > 0:
            print(f"WARNING: {duplicate_count} duplicate record_id(s) found.")
        else:
            print(f"No duplicate record_id.")

    # Check date parsing (just try to parse without changing original)
    if "date" in data.columns:
        invalid_date_rows = data[~pd.to_datetime(data["date"], errors="coerce").notna()]
        print(f"Invalid dates: {len(invalid_date_rows)} rows")
        if len(invalid_date_rows) > 0:
            print(invalid_date_rows[["record_id", "date"]])

    # Check numeric columns
    for column in data.select_dtypes(include=["float", "int"]):
        if data[column].isna().any():
            print(f"  Column '{column}' has {data[column].isna().sum()} missing or non-numeric values.")

    print(f"Validation finished for {filename}.\n")


if __name__ == "__main__":
    for dataset in DATASETS:
        validate_dataset(dataset)