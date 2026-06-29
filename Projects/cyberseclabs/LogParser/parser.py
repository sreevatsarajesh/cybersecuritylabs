def parse_line(line: str) -> dict:
    line = line.strip()

    if not line:
        return {}

    if ":" not in line:
        return {
            "error": "Invalid log format",
            "raw": line
        }

    header, message = line.split(": ", 1)

    parts = header.split()

    if len(parts) < 5:
        return {
            "error": "Malformed header",
            "raw": line
        }

    timestamp = " ".join(parts[:3])

    host = parts[3]

    service = parts[4]

    return {
        "timestamp": timestamp,
        "host": host,
        "service": service,
        "message": message.strip()
    }