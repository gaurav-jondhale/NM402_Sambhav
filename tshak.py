
# import pyshark

# cap  = pyshark.LiveCapture(interface = 'lo')

# for pkt in enumerate(cap):
#     if 'ip' in pkt:
#         print (pkt,flush = True)
# cap.close()

from scapy.all import *

#each time will be called when fresh packet arrives
def pkt_callback(pkt):
    pkt.show()
    print('rrrrrrrrrrrrrrrrrrssssssssssssssssssssppppppppppppppppp') # debug statement

#for packet sniffing
sniff(iface="wlp3s0", prn=pkt_callback, filter="tcp", store=0)