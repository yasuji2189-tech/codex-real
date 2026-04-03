import argparse
import csv
import json
import os
from pathlib import Path
from src.app import greet, greet_many
from src.transactions import load_transactions_csv, normalize_transactions, to_journal_candidates
from src.version import APP_VERSION

parser = argparse.ArgumentParser(description="Simple greeting CLI")
parser.add_argument("name", nargs="?", default=None, help="name to greet")
parser.add_argument("--many", nargs="*", help="greet multiple names")
parser.add_argument("--from-file", dest="from_file", help="read names from a text file")
parser.add_argument("--from-csv", dest="from_csv", help="read names from a csv file")
parser.add_argument("--csv-column", dest="csv_column", default="name", help="csv column name")
parser.add_argument("--tx-csv", dest="tx_csv", help="read transaction csv")
parser.add_argument("--tx-date-col", dest="tx_date_col", default="date", help="transaction date column")
parser.add_argument("--tx-desc-col", dest="tx_desc_col", default="description", help="transaction description column")
parser.add_argument("--tx-amount-col", dest="tx_amount_col", default="amount", help="transaction amount column")
parser.add_argument("--tx-journal", action="store_true", help="convert transaction csv to journal candidates")
parser.add_argument("--config", help="read settings from a json file")
parser.add_argument("--json", action="store_true", help="output as json")
parser.add_argument("--version", action="store_true", help="show app version")
parser.add_argument("--about", action="store_true", help="show app info")
args = parser.parse_args()

config = {}
if args.config:
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))

if "default_name" in config:
    os.environ["APP_DEFAULT_NAME"] = str(config["default_name"])
if "greeting_prefix" in config:
    os.environ["APP_GREETING_PREFIX"] = str(config["greeting_prefix"])

json_output = args.json or bool(config.get("json_output", False))

if args.about:
    result = {
        "app": "codex-real",
        "version": APP_VERSION,
        "supports": ["single", "many", "from-file", "from-csv", "tx-csv", "tx-journal", "config", "json", "env"],
    }
elif args.version:
    result = APP_VERSION
elif args.tx_csv:
    rows = load_transactions_csv(
        args.tx_csv,
        date_col=args.tx_date_col,
        desc_col=args.tx_desc_col,
        amount_col=args.tx_amount_col,
    )
    result = to_journal_candidates(rows) if args.tx_journal else normalize_transactions(rows)
elif args.from_file:
    names = [
        line.strip()
        for line in Path(args.from_file).read_text(encoding="utf-8").splitlines()
        if line.strip() != ""
    ]
    result = greet_many(names)
elif args.from_csv:
    names = []
    with open(args.from_csv, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            value = (row.get(args.csv_column) or "").strip()
            if value != "":
                names.append(value)
    result = greet_many(names)
elif args.many is not None:
    result = greet_many(args.many)
elif args.name is not None:
    result = greet(args.name)
elif "many_names" in config:
    result = greet_many(config["many_names"])
else:
    result = greet(None)

if json_output:
    print(json.dumps(result, ensure_ascii=False))
else:
    if isinstance(result, list):
        for line in result:
            if isinstance(line, dict) and "debit_account" in line:
                print(f"{line['date']},{line['debit_account']},{line['debit_amount']},{line['credit_account']},{line['credit_amount']},{line['description']},{line['tax_category']}")
            elif isinstance(line, dict):
                print(f"{line['date']},{line['description']},{line['amount']}")
            else:
                print(line)
    elif isinstance(result, dict):
        for k, v in result.items():
            print(f"{k}: {v}")
    else:
        print(result)
