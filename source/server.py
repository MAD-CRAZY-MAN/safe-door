import socket
import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = '172.30.1.31' # server socket`s IP
TCP_PORT = 20000       # server socket`s PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket 
sock.bind((TCP_IP, TCP_PORT)) # bind socket to IP, port
sock.listen(True) # wait client
client, addr = s.accept() # accept client, client = clilent`s socket, addr = client`s address 

length = recvall(client,16) # read
stringData = recvall(client, int(length))
data = numpy.fromstring(stringData, dtype='uint8')
sock.close()

decimg=cv2.imdecode(data,1) # decoding
cv2.imshow('SERVER',decimg) # show image

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
    
cv2.destroyAllWindows() 
