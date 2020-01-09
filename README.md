## ARP Poisoning Tool 

[![](https://img.shields.io/github/issues/EmreOvunc/ARP-Poisoning-Tool)](https://github.com/EmreOvunc/ARP-Poisoning-Tool/issues)
[![](https://img.shields.io/github/stars/EmreOvunc/ARP-Poisoning-Tool)](https://github.com/EmreOvunc/ARP-Poisoning-Tool/stargazers)
[![](https://img.shields.io/github/forks/EmreOvunc/ARP-Poisoning-Tool)](https://github.com/EmreOvunc/ARP-Poisoning-Tool/network/members)

Python SYN Flood Attack Tool

You can start SYN Flood attack with this tool.

Simple and efficient.

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
```


It uses SCAPY to generate fake ICMP and ARP packets.
The things which you need only are Destination IP and MAC address.

**Needs "root" privileges.**

It creates entries on target's ARP Table.

```
News v1.2:
***Auto ARP Generation Mode is added***
```

![alt tag](https://emreovunc.com/projects/ARP-Poisoning.jpeg)
