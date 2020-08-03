import socket, pickle, sys

if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number",flush = True)
	exit(0) 

IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2])

print ("Server is Listening.....")
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind((IP_address, Port))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)

data = conn.recv(4096)
data_variable = pickle.loads(data)
conn.close()
print (data_variable)
print ('Data received from client')