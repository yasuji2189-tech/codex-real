#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "PWD: $(pwd)"
echo "Python: $(python --version)"
echo "Git branch:"
git branch --show-current
echo "Git status:"
git status --short
echo "Tests:"
pytest -q
