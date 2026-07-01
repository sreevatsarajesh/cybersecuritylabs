import json
from pathlib import Path
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)
def print_results(results: dict):
    print("\n" + "=" * 60)
    print("IOC Extraction Results")
    print("=" * 60)
    for ioc_type, values in results.items():
        print(f"\n{ioc_type.upper()} ({len(values)})")
        if values:
            for value in values:
                print(f"  - {value}")
        else:
            print("  None")
def export_json(results: dict, filename="results.json"):
    output_file = OUTPUT_DIR / filename
    with open(output_file, "w") as file:
        json.dump(results, file, indent=4)
    print(f"\nResults exported to {output_file}")