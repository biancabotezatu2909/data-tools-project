# File Integrity Verification

## What are Checksums?
A checksum is a unique "fingerprint" of a file. If even one character changes in the file, the checksum will be completely different. This helps us:
- Detect file corruption
- Verify files haven't been accidentally modified
- Ensure data integrity over time

## Our Checksums
Location: `docs/checksums.sha256`

Generated on: 2026-01-11

Files protected:
- data/raw/records_2022.csv
- data/raw/records_2023.csv

## How to Verify Checksums

### Mac/Linux:
```bash
# Verify all checksums
shasum -a 256 -c docs/checksums.sha256

# Expected output if files are intact:
# data/raw/records_2022.csv: OK
# data/raw/records_2023.csv: OK

```


## When to Verify
- After copying files to a new location
- Before starting analysis (ensure data hasn't changed)
- If you suspect file corruption
- Periodically as part of data governance

## What if Verification Fails?
If checksums don't match:
1. DO NOT use the data for analysis
2. Check if the raw files were accidentally modified
3. Restore from backup or re-obtain from instructor
4. Document the incident in your project notes