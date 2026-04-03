# config precedence

## order
1. about
2. version
3. from-file
4. many
5. single name
6. config many_names
7. default name

## examples
python main.py --config config/sample.json yamada --json
python main.py --config config/sample.json --many ito kato --json
python main.py --config config/sample.json --from-file data/names.txt --json
