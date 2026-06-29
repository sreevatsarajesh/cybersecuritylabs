from parser import parse_line

LOG_FILE="sample_logs/sample.log"

with open(LOG_FILE,"r") as file:
    for line in file:
        parsed = parse_line(line)

        print(parsed)