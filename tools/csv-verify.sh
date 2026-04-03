#!/usr/bin/env bash
set -e
source .venv/bin/activate
python main.py --from-csv data/sample_names.csv
python main.py --from-csv data/sample_names.csv --json
python main.py --from-csv data/sample_names.csv --about --json
python main.py --from-csv data/sample_names.csv --version --json
pytest -q
