# Data Dictionary: Hospital Records Dataset



**Dataset:** records_2022.csv, records_2023.csv  

**Last Updated:** 2026-01-11



## Column Definitions



| Column Name   | Data Type | Description                             | Example Values                                 | Missing Values   |
|---------------|-----------|-----------------------------------------|-----------------------------------------------|----------------|
| record_id     | String    | Unique identifier for each record       | R0001606, R0002597                            | None allowed    |
| date          | Date      | Date of record (multiple formats found) | 2023-04-26, 12/10/2023                        | None observed   |
| category      | String    | Type of record                           | medication, billing                            | None observed   |
| value         | Numeric   | Quantity or amount                       | 203, 980.17, 2386.02                          | None observed   |
| unit          | String    | Unit of measurement                      | ml, dose, SEK, EUR                             | None observed   |
| source_system | String    | Origin system (case inconsistent)        | SYSTEM_A, manual_entry, import_batch, system_c| None observed   |
| status        | String    | Record status (case inconsistent)        | OK, ok, cancelled                              | None observed   |
| department    | String    | Department code                          | RAD, WARD_B, ICU, ADMIN                        | None observed   |
| priority      | String    | Priority level                           | high, medium                                   | None observed   |


## Data Quality Notes



### Issues Identified:

1. **Date Format Inconsistency**: Multiple date formats present

&nbsp;  - Format 1: YYYY-MM-DD (e.g., 2023-04-26)

&nbsp;  - Format 2: DD/MM/YYYY (e.g., 23/11/2023)

&nbsp;  - Format 3: M/D/YYYY (e.g., 1/29/2023)



2. **Case Inconsistency**: 

&nbsp;  - `source_system`: SYSTEM_A vs system_a vs system_c

&nbsp;  - `status`: OK vs ok



3. **Mixed Units**: 

&nbsp;  - Medication: ml, dose

&nbsp;  - Billing: SEK, EUR



### Business Rules:

- record_id follows pattern: R + 7 digits

- category values: {medication, billing}

- priority values: {high, medium} (low not observed)

- Cancelled records should be excluded from financial reporting



## Value Ranges (observed)

- Medication values: 203-980.17

- Billing values: 2386.02-2756.34

- Years covered: 2022-2023

