import scapy.all as scapy
import myModule as md
import optparse as op
from rich.console import Console
from rich.table import Table

md.credit();
#1)arp request
#2)Broadcast
#2)arp response

def get_user_input():
    parse_object = op.OptionParser();
    parse_object.add_option("-i", "--ipadress", dest="ip_address", help="Enter ip adress range");
    (user_input,arguments) = parse_object.parse_args();

    if not user_input.ip_address:
        print("[-] Please enter an ip address");
    return user_input;


def scan_my_network(ip):
    #"192.168.1.43/24"
    arp_request_packet = scapy.ARP(pdst=str(ip))
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet, timeout=1)

    table = Table(title="ARP Table")
    table.add_column("IP", style="cyan", justify="center")
    table.add_column("MAC", style="cyan", justify="center")
    for element in answered_list:
        table.add_row(element[1].psrc,element[1].hwsrc)
    console = Console()
    console.print(table)



user_ip_adress = get_user_input();
scan_my_network(user_ip_adress.ip_address)
