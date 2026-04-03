#!/usr/bin/env bash
set -e
source .venv/bin/activate
if [ -f .env ]; then
  set -a
  source .env
  set +a
fi

if [ $# -eq 0 ]; then
  python main.py
else
  python main.py "$1"
fi
