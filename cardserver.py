from operator import truediv
import socket

HOST = '127.0.0.1'
PORT = 65432

  #function using luhn's algorithm to check if card data recieved is valid
    #if valid, send back a message to the client
    #if not valid, send back a message to the client
def check_card(cardinfo):
    nDigits = len(cardinfo)
    nSum = 0
    isSecond = False
    #convert cardinfo to a list
    cardinfo = list(cardinfo)
    #convert all elements in cardinfo to integers
    cardinfo = [int(i) for i in cardinfo]
    #reverse the list
    cardinfo.reverse()
    #loop through the list
    for i in range(nDigits):
        #if isSecond is true, double the value of the element
        if isSecond == True:
            cardinfo[i] = cardinfo[i] * 2
        #add the value of the element to nSum
        nSum += cardinfo[i] // 10
        nSum += cardinfo[i] % 10
        #flip the value of isSecond
        isSecond = not isSecond
    #if nSum is divisible by 10, the card is valid
    if (nSum % 10 == 0):
        return True
    #if nSum is not divisible by 10, the card is not valid
    

opencon = True
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn: 
        print('Connected by', addr)
        while opencon == True:
            data = conn.recv(4096).decode()
            
            #send recieved data to check_card function
            if not data:
                break
            if check_card(data) == True:
                conn.sendall(b'Valid card')
                conn.sendall(b'connection terminated')
                opencon = False
                conn.close()
            else:
                conn.sendall(b'Invalid card')
                
                opencon = False
                conn.close()     
        socket.socket.close(s)
