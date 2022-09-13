#Make a client that connects to a server and sends a message

import socket
from xmlrpc.client import boolean

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
closecon = False
cardinfo = input("Enter card info: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
while closecon != True:
   #send card info to server
    client.send(cardinfo.encode())
    #receive response from server
    data = client.recv(4096)
    print(data.decode())
    closecon = True
client.close()
   
   


    