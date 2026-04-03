#!/usr/bin/env bash
set -e
source .venv/bin/activate
python main.py --help
python main.py --version
python main.py --about --json
python main.py --config config/sample.json --json
python main.py --from-csv data/sample_names.csv --json
pytest -q
git status
