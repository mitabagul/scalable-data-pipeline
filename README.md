# Scalable Data Pipeline

## Problem Statement
Build a small, maintainable ETL pipeline that ingests raw data, applies explicit transformations, and produces analytics-ready outputs.

## Architecture
The pipeline follows a clear Extract → Transform → Load (ETL structure):
- **Extract:** Reads raw data with minimal validation
- **Transform:** Applies explicit cleaning (date parsing, numeric casting, missing values)
- **Load:** Writes processed outputs to disk

Configuration (paths, filenames) is externalized via YAML to avoid hardcoding.

## How to Run
1. Install dependencies:
   - `python3 -m pip install -r requirements.txt`
2. Run the pipeline:
   - `python3 main.py`
3. Output:
   - Processed data is written to `data/processed/orders_processed.csv`

## Data Quality
- Required columns are validated
- Missing numeric values are handled explicitly
- Basic unit test included for transformations

## Trade-offs & Assumptions
- Optimized for clarity and modularity over performance
- File-based inputs for simplicity; can be extended to other sources


