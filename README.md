# codex-real

A small practical greeting CLI with:
- single input
- many input
- text file input
- csv input
- config json input
- json output
- version output
- about output
- env variable support
- helper scripts
- pytest coverage

## quick start
wsl
cd ~/work/codex-real
./tools/start.sh

## basic commands
python main.py
python main.py sasaki
python main.py --many sasaki tanaka

## file input
python main.py --from-file data/names.txt
python main.py --from-csv data/sample_names.csv
python main.py --from-csv data/sample_names.csv --csv-column name

## config input
python main.py --config config/sample.json
python main.py --config config/sample.json yamada
python main.py --config config/sample.json --many ito kato --json

## output options
python main.py --json
python main.py --about
python main.py --about --json
python main.py --version
python main.py --version --json

## environment variables
APP_DEFAULT_NAME=tanaka python main.py
APP_GREETING_PREFIX=goodbye python main.py sasaki
APP_DEFAULT_NAME=tanaka APP_GREETING_PREFIX=goodbye python main.py --many "" sasaki

## helper scripts
./tools/start.sh
./tools/preflight.sh
./tools/report.sh
./tools/final-check.sh
./tools/run.sh
./tools/run-many.sh
./tools/run-env.sh
./tools/version.sh
./tools/about.sh
./tools/demo.sh
./tools/prefix-demo.sh
./tools/env-demo.sh
./tools/config-demo.sh
./tools/config-verify.sh
./tools/csv-demo.sh
./tools/csv-verify.sh

## tests
pytest -q

## current version
0.1.1
