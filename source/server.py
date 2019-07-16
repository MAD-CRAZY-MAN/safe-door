import socket
import cv2
import numpy
from datetime import datetime
from time import sleep

def recvall(sock, count): # count만큼 데이터를 읽어서 buf에 저장하고 반환하는 함수
    buf = b''
    while count:
        newbuf = sock.recv(count) # count byte만큼 데이터를 읽어서 저장한다
        if not newbuf: return 0 # newbuf에 저장된 값이 없으면 결과 값없음을 반환
        buf += newbuf
        count -= len(newbuf) # 함수를 빠져나감 
    return buf

def init():
    global TCP_IP, TCP_PORT
    global sock, client
    
    TCP_IP = '192.168.137.168' # server socket`s IP
    TCP_PORT = 20000       # server socket`s PORT
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket 
    sock.bind((TCP_IP, TCP_PORT)) # bind socket to IP, port
    print('bind complete')
    
    sock.listen(1) # wait client
    client, addr = sock.accept() # accept client, client = clilent`s socket, addr = client`s address 
    print('accept complete')
    
    return None

init()


while True:
    length = recvall(client, 16) # read (socket, bytes), length = data`s size

    if not length == 0:
        stringData = recvall(client, int(length)) # 이미지의 길이만큼 데이터를 읽음

    
    if not stringData == 0:
        data = numpy.frombuffer(stringData, dtype='uint8') # 문자열 자료형으로부터 unsinged int형으로 변환

            
        decimg = cv2.imdecode(data, 1) # decoding

        cv2.namedWindow('CCTV', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('CCTV', 2500, 1000)
        cv2.imshow('CCTV', decimg) # show image
        cv2.moveWindow('CCTV', 0, 0)
        cv2.waitKey(0) # 아무키나 누르
        cv2.destroyAllWindows()
        now = datetime.now()
      
        Hour = now.strftime("%H")
        Min = now.strftime("%M")
        Sec = now.strftime("%S")
        cv2.imwrite("../../../list/%02d-%02d-%02d.jpg" % (int(Hour), int(Min), int(Sec)), decimg) # 바탕화면/list에 시간-분-초.jpg로 저장
        
        

sock.close()
