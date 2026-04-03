import sys
from src.app import greet

name = sys.argv[1] if len(sys.argv) > 1 else None
print(greet(name))
