import pyshark

pkts = pyshark.FileCapture('knockd.pcap')
a=[]
for p in pkts:
    if hasattr(p, 'tcp'):
        if str(p.tcp.srcport)+"--"+str(p.tcp.dstport) not in a and str(p.tcp.dstport)+"--"+str(p.tcp.srcport) not in a:
            a.append(p.tcp.srcport)
            a.append(p.tcp.dstport)
a = set(a)
f = open("ports.txt","w")
for i in a:
    f.write(i+'\n')