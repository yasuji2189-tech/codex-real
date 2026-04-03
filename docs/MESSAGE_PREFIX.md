# message prefix

## default prefix
python main.py sasaki

## env prefix
APP_GREETING_PREFIX=goodbye python main.py sasaki

## env prefix many
APP_GREETING_PREFIX=goodbye python main.py --many sasaki tanaka

## env prefix json
APP_GREETING_PREFIX=goodbye python main.py sasaki --json
