from parser import parse_line
from utils import get_log_path, read_log_file

LOG_FILE = get_log_path("sample.log")

lines = read_log_file(LOG_FILE)

for line in lines:
    parsed = parse_line(line)
    print(parsed)