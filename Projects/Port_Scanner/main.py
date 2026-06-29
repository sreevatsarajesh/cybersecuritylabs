from scanner import scan_port
from utils import get_service_name
HOST = "scanme.nmap.org"
PORTS = [20,21,22,23,25,53,80,110,143,443]
for port in PORTS:

    if scan_port(HOST, port):
        print(f"{port:<5} OPEN    {get_service_name(port)}")

    else:
        print(f"{port:<5} CLOSED  {get_service_name(port)}")
