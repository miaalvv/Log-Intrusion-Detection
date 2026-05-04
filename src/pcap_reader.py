#Uses the scapy library to read sample.pcap
from scapy.all import rdpcap

def summarize_pcap(path):
    packets = rdpcap(path)
    print(f"[INFO] Loaded {len(packets)} packets from {path}")
    return {"total_packets": len(packets)}