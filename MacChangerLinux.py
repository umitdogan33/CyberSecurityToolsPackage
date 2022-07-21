import subprocess as sp
import myModule as md
import optparse as op
import re

md.credit();

def get_user_input():
    parse_object = op.OptionParser();
    parse_object.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address");
    parse_object.add_option("-m", "--mac", dest="new_mac", help="New MAC address");
    return parse_object.parse_args();

def change_mac_address(interface,new_mac):
    sp.call(["ifconfig", interface, "down"]);
    sp.call(["ifconfig", interface, "hw", "ether",new_mac]);
    sp.call(["ifconfig", interface, "up"]);

def control_new_mac(interface):
    ifconfig = sp.sp.check_output(["ifconfig", interface]);
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig));

    if new_mac:
        return new_mac.group(0); # return the new mac address
    else:
        return None;


(options, arguments) = get_user_input();
interface = options.interface;
new_mac = options.new_mac;
change_mac_address(interface,new_mac);
final_mac = control_new_mac(str(interface));

if final_mac == new_mac:
    print("[+] MAC address was successfully changed to " + new_mac);
else:
    print("[-] MAC address was not changed");