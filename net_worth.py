"""Net worth tracker.

Reads networth.csv (date,assets,liabilities) and prints net worth over time.

Usage:
    python net_worth.py
    python net_worth.py --file my_history.csv
"""
import argparse
import csv


def load(path):
    rows = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            assets = float(row["assets"])
            liabilities = float(row["liabilities"])
            rows.append({
                "date": row["date"],
                "assets": assets,
                "liabilities": liabilities,
                "net_worth": round(assets - liabilities, 2),
            })
    return rows


def main():
    p = argparse.ArgumentParser(description="Net worth tracker")
    p.add_argument("--file", default="networth.csv")
    a = p.parse_args()
    rows = load(a.file)
    print("Date       |    Assets | Liabilities |  Net worth | Change")
    prev = None
    for r in rows:
        change = "" if prev is None else f"{r['net_worth'] - prev:+,.2f}"
        print(f"{r['date']} | {r['assets']:>9,.2f} | {r['liabilities']:>11,.2f} | "
              f"{r['net_worth']:>10,.2f} | {change:>10}")
        prev = r["net_worth"]
    if len(rows) >= 2:
        print(f"\nTotal change: {rows[-1]['net_worth'] - rows[0]['net_worth']:+,.2f} "
              f"over {len(rows)} records.")


if __name__ == "__main__":
    main()
