from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        print(
            f"{packet[IP].src} -> "
            f"{packet[IP].dst} | "
            f"Proto: {packet[IP].proto}"
        )

sniff(prn=packet_callback, store=False)