import os
from pathlib import Path

print(os.getcwd())
ROOT_DIR = Path(__file__).resolve().parent.parent
print(ROOT_DIR)