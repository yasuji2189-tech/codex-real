# workflow

## daily start
cd ~/work/codex-real
source .venv/bin/activate

## run
python main.py
python main.py sasaki

## test
pytest -q

## full check
./tools/check.sh

## git update
git add .
git commit -m "update"
git push
