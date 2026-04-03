#!/usr/bin/env bash
set -e
source .venv/bin/activate
python main.py --version
python main.py --about --json
python main.py --config config/sample.json --json
pytest -q
git status
