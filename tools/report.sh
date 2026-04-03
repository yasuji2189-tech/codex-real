#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "[version]"
python main.py --version
echo "[about]"
python main.py --about --json
echo "[config]"
python main.py --config config/sample.json --json
echo "[csv]"
python main.py --from-csv data/sample_names.csv --json
echo "[tests]"
pytest -q
