start:
	./tools/start.sh

test:
	pytest -q

preflight:
	./tools/preflight.sh

report:
	./tools/report.sh

final-check:
	./tools/final-check.sh

run:
	python main.py

run-many:
	python main.py --many sasaki tanaka

run-config:
	python main.py --config config/sample.json

run-csv:
	python main.py --from-csv data/sample_names.csv
