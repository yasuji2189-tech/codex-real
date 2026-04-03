#!/usr/bin/env bash
set -e
source .venv/bin/activate
if [ $# -eq 0 ]; then
  python main.py
else
  python main.py "$1"
fi
