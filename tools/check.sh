#!/usr/bin/env bash
set -e
source .venv/bin/activate
python main.py
python main.py sasaki
python scripts/test_request.py
pytest -q
git status
