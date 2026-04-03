import argparse
from src.app import greet, greet_many

parser = argparse.ArgumentParser(description="Simple greeting CLI")
parser.add_argument("name", nargs="?", default=None, help="name to greet")
parser.add_argument("--many", nargs="*", help="greet multiple names")
args = parser.parse_args()

if args.many is not None:
    for line in greet_many(args.many):
        print(line)
else:
    print(greet(args.name))
