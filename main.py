import argparse
from src.app import greet

parser = argparse.ArgumentParser(description="Simple greeting CLI")
parser.add_argument("name", nargs="?", default=None, help="name to greet")
args = parser.parse_args()

print(greet(args.name))
