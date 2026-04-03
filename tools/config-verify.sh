#!/usr/bin/env bash
set -e
source .venv/bin/activate
python main.py --config config/sample.json
python main.py --config config/sample.json yamada --json
python main.py --config config/sample.json --about --json
python main.py --config config/sample.json --version --json
pytest -q
