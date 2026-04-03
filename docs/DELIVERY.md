# delivery

## ready commands
./tools/start.sh
./tools/preflight.sh
./tools/report.sh

## main use cases
python main.py
python main.py sasaki
python main.py --many sasaki tanaka
python main.py --from-file data/names.txt
python main.py --from-csv data/sample_names.csv
python main.py --config config/sample.json

## output options
python main.py --json
python main.py --about --json
python main.py --version --json
