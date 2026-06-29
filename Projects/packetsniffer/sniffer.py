from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

sniff(
    prn=packet_callback,
    store=False,
    count=20
)

print("Captured 20 packets. Stopping.")