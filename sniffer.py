from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

LOG_FILE = "capture_log.txt"
SERVICES = {80: "HTTP", 443: "HTTPS", 53: "DNS", 22: "SSH", 21: "FTP", 25: "SMTP"}

def show_packet(packet):
    if IP not in packet:
        return

    time = datetime.now().strftime("%H:%M:%S")
    src = packet[IP].src
    dst = packet[IP].dst
    service = "-"

    if TCP in packet:
        proto = "TCP"
        sport, dport = packet[TCP].sport, packet[TCP].dport
        ports = f"{sport} -> {dport}"
        service = SERVICES.get(sport) or SERVICES.get(dport) or "-"
    elif UDP in packet:
        proto = "UDP"
        sport, dport = packet[UDP].sport, packet[UDP].dport
        ports = f"{sport} -> {dport}"
        service = SERVICES.get(sport) or SERVICES.get(dport) or "-"
    elif ICMP in packet:
        proto = "ICMP"
        ports = "-"
    else:
        proto = str(packet[IP].proto)
        ports = "-"

    line = f"{time} [{proto}/{service}] {src} -> {dst} | ports: {ports}"

    if Raw in packet:
        data = bytes(packet[Raw].load)[:16].hex(" ")
        line += f" | payload (hex): {data}"

    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

print("Sniffer running... press Ctrl+C to stop.")
try:
    sniff(prn=show_packet, store=False)
except KeyboardInterrupt:
    print("\nStopped. Log saved to", LOG_FILE)