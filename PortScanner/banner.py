from scanner import scan_port
import socket

def grab_banner(host:str,port:int,timeout:int =3):
    if not scan_port(host,port,timeout):
        return None
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.settimeout(timeout)
        sock.connect((host,port))
        banner = sock.recv(1024).decode(errors="ignore")
        return banner.strip()
    finally:
        sock.close()
