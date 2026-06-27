def parse_ssh_banner(banner:str) -> dict:
    protocol, protocol_version, software = banner.split("-",2)
    software_name,software_version = software.split("_",1)
    return {
        "protocol": protocol,
        "protocol_version":protocol_version,
        "software":software_name,
        "software_version":software_version,
        "raw_banner":banner
    }
def parse_http_banner(banner: str) -> dict:
    parts = banner.split()

    return {
        "protocol": parts[0],
        "status_code": parts[1] if len(parts) > 1 else None,
        "status": " ".join(parts[2:]) if len(parts) > 2 else None,
        "raw_banner": banner
    }


