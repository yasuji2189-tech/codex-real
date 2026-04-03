#!/usr/bin/env bash
set -e
cd ~/work/codex-real
source .venv/bin/activate
echo "ready"
echo "project: $(pwd)"
echo "branch: $(git branch --show-current)"
