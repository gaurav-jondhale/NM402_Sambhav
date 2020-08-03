import socket, pickle, sys
from processdata import ProcessData

if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number",flush = True)
	exit(0) 

IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2])

# Create a socket connection.
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((IP_address, Port))

# Create an instance of ProcessData() to send to server.
variable = ProcessData()
# Pickle the object and send it to the server
data_string = pickle.dumps(variable)
s.send(data_string)

s.close()
print ('Data Sent to Server')