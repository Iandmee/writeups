import pyshark

pkts = pyshark.FileCapture('cap.pcap')

for p in pkts:
    if hasattr(p, 'tcp'):
        print(p.tcp.dstport)