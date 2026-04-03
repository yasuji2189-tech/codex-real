import argparse
import json
from src.app import greet, greet_many
from src.version import APP_VERSION

parser = argparse.ArgumentParser(description="Simple greeting CLI")
parser.add_argument("name", nargs="?", default=None, help="name to greet")
parser.add_argument("--many", nargs="*", help="greet multiple names")
parser.add_argument("--json", action="store_true", help="output as json")
parser.add_argument("--version", action="store_true", help="show app version")
args = parser.parse_args()

if args.version:
    result = APP_VERSION
elif args.many is not None:
    result = greet_many(args.many)
else:
    result = greet(args.name) if args.json:
    print(json.dumps(result, ensure_ascii=False))
else:
    if isinstance(result, list):
        for line in result:
            print(line)
    else:
        print(result)
