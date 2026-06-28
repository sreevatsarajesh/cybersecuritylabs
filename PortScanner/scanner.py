import socket

def scan_port(host: str, port :int,timeout: int=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(3)
        result = sock.connect_ex((HOST,PORT))
        return result==0
    finally:
        sock.close()