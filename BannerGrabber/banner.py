from scanner import grab_banner
from parser import parse_banner
from utils import (
    validate_port,
    resolve_hostname,
    print_banner,
)

HOST = "scanme.nmap.org"
PORT = 22

if not validate_port(PORT):
    raise ValueError(f"Invalid port: {PORT}")

IP = resolve_hostname(HOST)

banner = grab_banner(HOST, PORT)

info = parse_banner(banner)

print_banner("Banner Grabber")

print(f"Host              : {HOST}")
print(f"IP Address        : {IP}")
print(f"Port              : {PORT}")
print(f"Protocol          : {info.get('protocol')}")
print(f"Raw Banner        : {info.get('raw_banner')}")