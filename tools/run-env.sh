#!/usr/bin/env bash
set -e
source .venv/bin/activate
if [ -f .env ]; then
  set -a
  source .env
  set +a
fi
python main.py "${1:-}"
