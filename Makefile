setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	. .venv/bin/activate && python main.py

run-sasaki:
	. .venv/bin/activate && python main.py sasaki

test:
	. .venv/bin/activate && pytest -q

check:
	. .venv/bin/activate && ./tools/check.sh
