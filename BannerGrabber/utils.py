import socket

def validate_port(port: int) -> bool:
    return 1 <= port <= 65535
def resolve_hostname(host: str) -> str:
    return socket.gethostbyname(host)
def is_ip(host: str) -> bool:
    try:
        socket.inet_aton(host)
        return True
    except socket.error:
        return False
def print_banner(title: str):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)