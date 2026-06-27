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

def parse_ftp_or_smtp_banner(banner: str) -> dict:
    message = banner[4:] if len(banner) > 4 else ""

    protocol = "UNKNOWN"

    if "ESMTP" in message or "SMTP" in message:
        protocol = "SMTP"
    elif "FTP" in message or "FileZilla" in message:
        protocol = "FTP"

    return {
        "protocol": protocol,
        "status_code": banner[:3],
        "message": message,
        "raw_banner": banner
    }

def parse_unknown_banner(banner: str) -> dict:
    return {
        "protocol": "UNKNOWN",
        "raw_banner": banner
    }

def parse_banner(banner: str) -> dict:
    banner = banner.strip()

    if banner.startswith("SSH-"):
        return parse_ssh_banner(banner)

    elif banner.startswith("HTTP/"):
        return parse_http_banner(banner)

    elif banner.startswith("220"):
        return parse_ftp_or_smtp_banner(banner)

    else:
        return parse_unknown_banner(banner)
