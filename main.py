import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent / 'src'))
from app import greet

name = sys.argv[1] if len(sys.argv) > 1 else 'world'
print(greet(name))
