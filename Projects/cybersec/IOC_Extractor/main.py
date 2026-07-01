from pathlib import Path
from extractor import extract_iocs
from parser import clean_results
from utils import print_results, export_json
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "sample_files" / "sample.txt"
with open(INPUT_FILE, "r") as file:
    text = file.read()
results = extract_iocs(text)
results = clean_results(results)
print_results(results)
export_json(results)