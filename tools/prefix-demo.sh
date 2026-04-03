#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "[default]"
python main.py sasaki
echo "[env-prefix]"
APP_GREETING_PREFIX=goodbye python main.py sasaki
echo "[many-env-prefix]"
APP_GREETING_PREFIX=goodbye python main.py --many sasaki tanaka
echo "[json-env-prefix]"
APP_GREETING_PREFIX=goodbye python main.py sasaki --json
