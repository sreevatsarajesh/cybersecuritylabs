def parse_line(line: str)->dict:
    line = line.strip()
    if not line:
        return {}
    
    header,message = line.split(":",1)
    parts = header.split()
    timestamp = " ".join(parts[:3])
    host = parts[3]
    service = parts[4]

    return {
        "timestamp":timestamp,
        "host":host,
        "service":service,
        "message":message.strip()
    }