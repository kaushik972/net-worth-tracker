# Net Worth Tracker

A small Python CLI that tracks net worth over time from a simple CSV.

## What it does
- Reads `networth.csv` (`date,assets,liabilities`)
- Prints assets, liabilities and net worth per record, with the change each month
- Total change across the whole history

## Run it
```bash
python net_worth.py
python net_worth.py --file my_history.csv
```

## Example
Aug–Nov 2026 sample data → net worth grows from 730,000 to **840,000**.

Built by Shivam Kaushik as a daily mini project — Python, no dependencies.
