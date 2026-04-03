# handoff

## ready state
- repo is on main
- tests pass
- helper scripts exist
- make targets exist
- config/json/csv/file input supported

## startup
wsl
cd ~/work/codex-real
./tools/start.sh

## verify
./tools/preflight.sh
./tools/report.sh
./tools/final-check.sh

## common commands
make run
make run-config
make run-csv
pytest -q
