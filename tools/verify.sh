#!/usr/bin/env bash
set -e
source .venv/bin/activate
python main.py --version
python main.py --about
python main.py --about --json
pytest -q
