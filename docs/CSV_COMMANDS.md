# csv commands

## basic
python main.py --from-csv data/sample_names.csv
python main.py --from-csv data/sample_names.csv --json

## custom column
python main.py --from-csv data/people.csv --csv-column person
python main.py --from-csv data/people.csv --csv-column person --json

## with config
python main.py --config config/sample.json --from-csv data/sample_names.csv --json
python main.py --config config/sample.json --from-csv data/combo_people.csv --csv-column person --json
