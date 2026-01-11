# src/generate_report.py

import os
import pandas as pd
from datetime import datetime

PROCESSED_DATA_DIR = "data/processed"
REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

REPORT_FILE = os.path.join(REPORTS_DIR, "summary_report.md")

DATASETS = {
    "Records 2022": os.path.join(PROCESSED_DATA_DIR, "records_2022_clean.csv"),
    "Records 2023": os.path.join(PROCESSED_DATA_DIR, "records_2023_clean.csv"),
}

def summarize_dataset(df: pd.DataFrame, dataset_name: str) -> list[str]:
    """
    Generate summary for a dataset including row/column counts, missing values, and category counts.
    Returns a list of Markdown-formatted strings.
    """
    summary_lines = [f"### {dataset_name}\n"]
    
    # Basic stats in table format
    summary_lines.append("| Metric | Value |")
    summary_lines.append("|--------|-------|")
    summary_lines.append(f"| Total Records | {len(df):,} |")
    summary_lines.append(f"| Total Columns | {len(df.columns)} |")
    
    # Date range if available
    if "date" in df.columns:
        date_col = pd.to_datetime(df["date"], errors='coerce')
        if date_col.notna().any():
            summary_lines.append(f"| Date Range | {date_col.min()} to {date_col.max()} |")
    
    summary_lines.append("")

    # Missing values in table format
    missing_data = df.isna().sum()
    if missing_data.sum() > 0:
        summary_lines.append("**Missing Values:**\n")
        summary_lines.append("| Column | Missing Count | Percentage |")
        summary_lines.append("|--------|---------------|------------|")
        for col, missing_count in missing_data.items():
            if missing_count > 0:
                pct = (missing_count / len(df)) * 100
                summary_lines.append(f"| {col} | {missing_count} | {pct:.1f}% |")
        summary_lines.append("")
    else:
        summary_lines.append("✅ **No missing values**\n")

    # Category distribution in table format
    if "category" in df.columns:
        summary_lines.append("**Category Distribution:**\n")
        summary_lines.append("| Category | Count | Percentage |")
        summary_lines.append("|----------|-------|------------|")
        total = len(df)
        for category, count in df["category"].value_counts().items():
            pct = (count / total) * 100
            summary_lines.append(f"| {category} | {count:,} | {pct:.1f}% |")
        summary_lines.append("")

    # Department distribution if available
    if "department" in df.columns and df["department"].notna().any():
        summary_lines.append("**Department Distribution:**\n")
        summary_lines.append("| Department | Count |")
        summary_lines.append("|------------|-------|")
        for dept, count in df["department"].value_counts().head(10).items():
            summary_lines.append(f"| {dept} | {count:,} |")
        summary_lines.append("")

    # Status distribution if available
    if "status" in df.columns and df["status"].notna().any():
        summary_lines.append("**Status Distribution:**\n")
        summary_lines.append("| Status | Count |")
        summary_lines.append("|--------|-------|")
        for status, count in df["status"].value_counts().items():
            summary_lines.append(f"| {status} | {count:,} |")
        summary_lines.append("")

    summary_lines.append("---\n")
    return summary_lines


def generate_report(datasets: dict[str, str], report_file: str) -> None:
    """
    Generate a Markdown summary report for multiple datasets.
    """
    report_content = ["# Hospital Records Data Pipeline"]
    report_content.append("## Summary Report\n")
    report_content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report_content.append("---\n")

    # Process each dataset
    for dataset_name, path in datasets.items():
        if os.path.exists(path):
            df = pd.read_csv(path)
            report_content += summarize_dataset(df, dataset_name)
        else:
            report_content.append(f"### {dataset_name}\n")
            report_content.append(f"⚠️ **File not found:** `{path}`\n\n---\n")

    # Add combined analysis if both files exist
    all_paths = [p for p in datasets.values() if os.path.exists(p)]
    if len(all_paths) > 1:
        report_content.append("## Combined Dataset Analysis\n")
        combined_df = pd.concat([pd.read_csv(p) for p in all_paths], ignore_index=True)
        report_content.append(f"**Total Records Across All Files:** {len(combined_df):,}\n")
        
        if "category" in combined_df.columns:
            report_content.append("\n**Overall Category Distribution:**\n")
            report_content.append("| Category | Total Count | Percentage |")
            report_content.append("|----------|-------------|------------|")
            total = len(combined_df)
            for category, count in combined_df["category"].value_counts().items():
                pct = (count / total) * 100
                report_content.append(f"| {category} | {count:,} | {pct:.1f}% |")

    with open(report_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_content))

    print(f"Report generated: {report_file}")

if __name__ == "__main__":
    generate_report(DATASETS, REPORT_FILE)