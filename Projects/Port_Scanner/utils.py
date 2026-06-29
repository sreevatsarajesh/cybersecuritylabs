import socket


COMMON_PORTS = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MYSQL",
    3389: "RDP",
    8080: "HTTP-ALT",
}

def resolve_hostname(host:str):
    return socket.gethostname(host)

def get_service_name(port: int):
    return COMMON_PORTS.get(port,"UNKNOWN")