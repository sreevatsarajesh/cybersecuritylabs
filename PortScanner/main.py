from scanner import scan_port
HOST = "scanme.nmap.org"

ports = [22,80,443]

for port in ports:
    if scan_port(HOST,port):
        print(f"{port} OPEN")
    else:
        print(f"{port} CLOSED")
