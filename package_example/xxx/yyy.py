
from pathlib import Path

import sys


BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))
print(sys.path)

from przestrzenie import hello_word

print(hello_word())

def foo():
    pass