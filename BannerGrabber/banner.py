import socket
s=socket.socket()
print ("Socket Created")
s.connect(("scanme.nmap.org",22))
banner = s.recv(1024)
print(banner.decode())
s.close()