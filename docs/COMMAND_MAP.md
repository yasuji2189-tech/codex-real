# command map

## startup
wsl
cd ~/work/codex-real
./tools/start.sh

## main commands
python main.py
python main.py sasaki
python main.py --many sasaki tanaka
python main.py --json
python main.py --version
python main.py --about

## helper scripts
./tools/run.sh
./tools/run-many.sh
./tools/run-env.sh
./tools/version.sh
./tools/about.sh
./tools/demo.sh
./tools/verify.sh

## tests
pytest -q
./tools/test.sh
./tools/test-all.sh
