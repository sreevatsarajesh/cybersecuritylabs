import socket


def validate_port(port: int) -> bool:
    """
    Checks if the port is valid.
    """

    return 1 <= port <= 65535


def resolve_hostname(host: str) -> str:
    """
    Resolves a hostname into an IPv4 address.
    """

    return socket.gethostbyname(host)


def is_ip(host: str) -> bool:
    """
    Returns True if the host is already an IPv4 address.
    """

    try:
        socket.inet_aton(host)
        return True
    except socket.error:
        return False


def print_banner(title: str):
    """
    Prints a formatted title.
    """

    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)