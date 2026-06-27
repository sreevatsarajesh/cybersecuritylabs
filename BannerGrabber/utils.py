import ipaddress
import socket


def validate_port(port: int) -> bool:
    return 1 <= port <= 65535


def resolve_hostname(host: str) -> str:
    return socket.gethostbyname(host)


def is_ip(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def print_banner(title: str):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)