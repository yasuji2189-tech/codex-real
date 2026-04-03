import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
from app import greet

def test_greet_default():
    assert greet() == 'hello, world'

def test_greet_name():
    assert greet('sasaki') == 'hello, sasaki'
