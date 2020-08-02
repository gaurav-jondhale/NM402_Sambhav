# from kp import *
import socket
import time,sys
import pickle


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
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            msg_rcvd = pickle.loads(full_msg[HEADERSIZE:])
            msg_rcvd.tellStatus()
            new_msg = True
            full_msg = b""