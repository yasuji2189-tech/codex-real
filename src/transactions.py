import csv
from pathlib import Path

def load_transactions_csv(path, date_col="date", desc_col="description", amount_col="amount"):
    rows = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = (row.get(date_col) or "").strip()
            description = (row.get(desc_col) or "").strip()
            amount_raw = (row.get(amount_col) or "").strip().replace(",", "")
            if not date and not description and not amount_raw:
                continue
            rows.append(
                {
                    "date": date,
                    "description": description,
                    "amount": amount_raw,
                }
            )
    return rows

def normalize_transactions(rows):
    normalized = []
    for row in rows:
        amount_text = str(row.get("amount", "")).strip()
        try:
            amount = int(float(amount_text)) if amount_text != "" else 0
        except ValueError:
            amount = 0
        normalized.append(
            {
                "date": str(row.get("date", "")).strip(),
                "description": str(row.get("description", "")).strip(),
                "amount": amount,
            }
        )
    return normalized
