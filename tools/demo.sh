#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "[single]"
python main.py
echo "[single-json]"
python main.py sasaki --json
echo "[many]"
python main.py --many sasaki tanaka
echo "[about]"
python main.py --about
echo "[version]"
python main.py --version
