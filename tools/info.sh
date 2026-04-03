#!/usr/bin/env bash
set -e
source .venv/bin/activate
echo "project: codex-real"
echo "pwd: $(pwd)"
echo "branch: $(git branch --show-current)"
echo "python: $(python --version)"
echo "pip: $(pip --version | head -n 1)"
echo "files:"
ls
echo "tests:"
pytest -q
