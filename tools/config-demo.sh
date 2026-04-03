#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "[config]"
python main.py --config config/sample.json
echo "[config-version]"
python main.py --config config/sample.json --version
echo "[config-many-override]"
python main.py --config config/sample.json --many ito kato --json
echo "[config-file]"
python main.py --config config/sample.json --from-file data/names.txt --json
