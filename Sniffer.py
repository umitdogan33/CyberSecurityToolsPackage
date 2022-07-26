import scapy.all as scapy;
from scapy_http import http;

def listen_packages():
    scapy.sniff(iface="wlan0",store=False,prn=analyze_packet)

def analyze_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.hashlayer(scapy.Raw):
            print(packet[scapy.Raw].load)
    return None;