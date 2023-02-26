import sys
import os

print("xxxx", os.path.dirname(os.path.dirname(__file__)))

from pathlib import Path

print(__file__)
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

print(BASE_DIR / "xxx" / "yyy")

sys.path.append(str(BASE_DIR))
print(sys.path)

from pkg1 import mod1

# from pkg1 import funkcja_z_package
