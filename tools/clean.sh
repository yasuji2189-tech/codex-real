#!/usr/bin/env bash
set -e
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
echo "cleaned"
