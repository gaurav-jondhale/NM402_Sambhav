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
s.bind((IP_address,Port))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = {1:"hi", 2: "there"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)