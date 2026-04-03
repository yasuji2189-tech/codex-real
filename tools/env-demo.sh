#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "[default-name]"
APP_DEFAULT_NAME=tanaka python main.py
echo "[prefix]"
APP_GREETING_PREFIX=goodbye python main.py sasaki
echo "[combined]"
APP_DEFAULT_NAME=tanaka APP_GREETING_PREFIX=goodbye python main.py
echo "[many-combined]"
APP_DEFAULT_NAME=tanaka APP_GREETING_PREFIX=goodbye python main.py --many "" sasaki
