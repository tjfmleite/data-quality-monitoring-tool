# Data Quality Monitoring Tool

## Overview
This project provides a Python-based tool to monitor data quality in banking datasets. It identifies issues such as missing values, invalid entries (e.g., negative balances or unrealistic ages), and generates a detailed data quality report for further analysis.

## Features
- Detect missing values in the dataset.
- Identify invalid ages (e.g., less than 0 or greater than 100).
- Flag accounts with negative balances.
- Generate a summary report of data issues and statistics.
- Save the findings in a detailed text report.

## Files
- `data_quality.csv`: Sample dataset for data quality checks.
- `data_quality_monitoring.py`: Python script to perform the analysis.
- `data_quality_report.txt`: Generated report with missing values, invalid data, and summary statistics.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/tjfmleite/data-quality-monitoring-tool.git
   cd data-quality-monitoring-tool
