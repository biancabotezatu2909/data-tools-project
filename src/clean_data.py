import os
from datetime import datetime

import pandas as pd

RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

CATEGORY_NORMALIZATION = {
    "ADMISSION": "Admission",
    "BILLING": "Billing",
    "DISCHARGE": "Discharge",
    "FOLLOW_UP": "Follow-up",
    "FOLLOW-UP": "Follow-up",
    "IMAGING": "Imaging",
    "LAB TEST": "Lab Test",
    "LAB_TEST": "Lab Test",
    "LABTEST": "Lab Test",
    "MEDICATION": "Medication",
    "TRANSFER": "Transfer"
}

DATE_FORMATS = [
    "%Y-%m-%d",  # ISO
    "%d/%m/%Y",  # 23/11/2023
    "%m/%d/%Y",  # 12/10/2023
    "%d-%m-%Y",  # optional
    "%m-%d-%Y",
]

def load_csv(filename: str) -> pd.DataFrame:
    path = os.path.join(RAW_DATA_DIR, filename)
    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, base_name: str) -> None:
    path = os.path.join(PROCESSED_DATA_DIR, f"{base_name}_clean.csv")
    df.to_csv(path, index=False)
    print(f"Saved CSV: {path}")

def clean_string_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Strip spaces in all string columns."""
    str_cols = df.select_dtypes(include=["object"])
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()
    return df

def parse_dates(df: pd.DataFrame, column_name="date") -> pd.DataFrame:
    """Parse dates in mixed formats."""
    if column_name not in df.columns:
        return df

    def try_parse_single(date_str):
        if pd.isna(date_str):
            return pd.NaT
        date_str = str(date_str).strip()
        for fmt in DATE_FORMATS:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return pd.NaT

    df[column_name] = df[column_name].apply(try_parse_single)
    return df

def normalize_categories(df: pd.DataFrame, column_name="category") -> pd.DataFrame:
    if column_name in df.columns:
        df[column_name] = df[column_name].astype(str).str.strip().str.upper()
        df[column_name] = df[column_name].replace(CATEGORY_NORMALIZATION)
    return df

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            continue  # keep NaT for dates
        elif pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col] = df[col].fillna("Unknown")
    return df

def drop_duplicate_records(df: pd.DataFrame, key="record_id") -> pd.DataFrame:
    if key in df.columns:
        df = df.drop_duplicates(subset=key, keep="first")
    return df

def align_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Ensure all target columns exist and are in correct order."""
    for col in columns:
        if col not in df.columns:
            df[col] = pd.NA
    return df[columns]

def process_file(filename: str, target_columns: list[str] = None) -> None:
    print(f"Processing {filename}...")
    df = load_csv(filename)
    df = clean_string_columns(df)
    df = parse_dates(df)
    df = normalize_categories(df)
    df = fill_missing_values(df)
    df = drop_duplicate_records(df)
    if target_columns:
        df = align_columns(df, target_columns)
    base_name = os.path.splitext(filename)[0]
    save_csv(df, base_name)
    print(f"{filename} processed successfully.\n")

if __name__ == "__main__":
    TARGET_COLUMNS = [
        "record_id", "date", "category", "value", "unit",
        "source", "source_system", "status", "department", "priority"
    ]

    DATASETS = ["records_2022.csv", "records_2023.csv"]

    for dataset_file in DATASETS:
        process_file(dataset_file, TARGET_COLUMNS)
