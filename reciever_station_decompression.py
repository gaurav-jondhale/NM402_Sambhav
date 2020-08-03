from packetClass import *
import socket
import time,sys
import pickle
from gethash import *

dict = {}

HEADERSIZE = 10

if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2])

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((IP_address, Port))


while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(4096)
        if new_msg:
            # print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        # print(f"full message length: {msglen}")

        full_msg += msg

        # print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            # print("full msg recvd")
            # print(full_msg[HEADERSIZE:])
            msg_rcv = pickle.loads(full_msg[HEADERSIZE:])
            if(msg_rcv.compressed == True):
                print("hid: ", msg_rcv.hid)
                st = dict[msg_rcv.hid]
                od = st.split()
                src = od[0]
                dst = od[1]
                sport = od[2]
                dport = od[3]
                version = od[4]
                proto = od[5]
                comp = tcpip(False, version, msg_rcv.ihl, msg_rcv.tos, msg_rcv.len, msg_rcv.id, msg_rcv.ipflags, msg_rcv.frag, msg_rcv.ttl, proto, msg_rcv.ipchksum, src, dst, msg_rcv.ipoptions, sport, dport, msg_rcv.seq, msg_rcv.ack, msg_rcv.dataofs, msg_rcv.reserved, msg_rcv.tcpflags, msg_rcv.window, msg_rcv.tcpchksum, msg_rcv.urgptr, msg_rcv.tcpoptions) 
            else:
                comp = msg_rcv
                st = comp.src + " " + comp.dst + " " + str(comp.sport) + " " + str(comp.dport) + " " + str(comp.version) + " " + str(comp.proto)
                # print(st)
                hid = hash1(st) & 0xffffffff
                print("predicted: ", hid)
                dict[hid] = st

            comp.tellStatus()
            # msg_rcv.tellStatus()
            new_msg = True
            full_msg = b''
