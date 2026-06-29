from pathlib import Path
from parser import parse_line

BASE_DIR = Path(__file__).parent
LOG_FILE = BASE_DIR / "sample_logs" / "sample.log"

with LOG_FILE.open("r") as file:
    for line in file:
        parsed = parse_line(line)
        print(parsed)