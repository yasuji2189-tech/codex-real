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

def guess_account(description: str) -> str:
    text = (description or "").lower()
    jp = description or ""
    if "taxi" in text or "jr" in text or "電車" in jp or "タクシ" in jp or "新幹線" in jp:
        return "旅費交通費"
    if "stationery" in text or "amazon" in text or "事務用品" in jp or "文具" in jp:
        return "消耗品費"
    if "lunch" in text or "会食" in jp or "昼食" in jp or "coffee" in text:
        return "会議費"
    if "eneos" in text or "gas" in text or "ガソリン" in jp:
        return "車両費"
    return "雑費"

def guess_tax_category(description: str) -> str:
    text = (description or "").lower()
    jp = description or ""
    if "taxi" in text or "jr" in text or "電車" in jp or "タクシ" in jp or "stationery" in text or "amazon" in text or "文具" in jp or "ガソリン" in jp:
        return "課税10%"
    if "lunch" in text or "会食" in jp or "昼食" in jp:
        return "課税10%"
    return "課税10%"

def to_journal_candidates(rows, credit_account="普通預金"):
    normalized = normalize_transactions(rows)
    out = []
    for row in normalized:
        out.append(
            {
                "date": row["date"],
                "debit_account": guess_account(row["description"]),
                "debit_amount": row["amount"],
                "credit_account": credit_account,
                "credit_amount": row["amount"],
                "description": row["description"],
                "tax_category": guess_tax_category(row["description"]),
            }
        )
    return out
