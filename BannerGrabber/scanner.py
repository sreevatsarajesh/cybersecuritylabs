import socket 

def grab_banner(host: str,port: int,timeout:int=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_Stream)
    sock