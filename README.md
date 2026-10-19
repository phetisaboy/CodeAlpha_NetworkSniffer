# CodeAlpha Network Sniffer

A basic network sniffer built in Python with Scapy. It captures live packets on your network and shows how data moves through it.

## Features

- Captures live IP packets (TCP, UDP, ICMP)
- Shows timestamp, protocol, source and destination IP, and ports
- Labels common services (HTTPS, DNS, HTTP, SSH, FTP, SMTP)
- Shows the first 16 bytes of each payload in hex
- Saves every captured packet to `capture_log.txt`
- Stops cleanly with Ctrl+C

## Requirements

- Python 3
- Scapy
- Windows: Npcap (installed with Wireshark)
- Linux/Mac: run with `sudo`

## Installation

```
git clone https://github.com/phetisaboy/CodeAlpha_NetworkSniffer.git
cd CodeAlpha_NetworkSniffer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run in a terminal (as administrator on Windows):

```
python sniffer.py
```

Press Ctrl+C to stop.

## Sample Output

```
07:21:01 [UDP/DNS] 10.222.221.19 -> 10.222.221.186 | ports: 57020 -> 53
07:21:01 [TCP/HTTPS] 10.222.221.19 -> 140.82.114.21 | ports: 12964 -> 443
```

## What I Learned

- How packets are structured (Ethernet, IP, TCP/UDP)
- Why HTTPS payloads look unreadable (TLS encryption)
- How DNS lookups happen before a connection starts

## Disclaimer

For educational use only. Only capture traffic on networks you own or have permission to monitor.

## Author

Aboderin Semilore Gold (phetboy), CodeAlpha Cyber Security Internship