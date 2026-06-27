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
