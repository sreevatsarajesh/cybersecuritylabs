import socket 

def grab_banner(host: str,port: int,timeout:int=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    sock.connect((host,port))

    banner=sock.recv(1024).decode(errors="ignore")

    sock.close()
    return banner