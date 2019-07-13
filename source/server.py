import socket
import cv2
import numpy
from datetime import datetime

def recvall(sock, count): # count만큼 데이터를 읽어서 buf에 저장하고 반환하는 함수
    buf = b''
    while count:
        newbuf = sock.recv(count) # count byte만큼 데이터를 읽어서 저장한다
        if not newbuf: return None # newbuf에 저장된 값이 없으면 결과 값없음을 반환
        buf += newbuf
        count -= len(newbuf) # 함수를 빠져나감 
    return buf

def init():
    global TCP_IP, TCP_PORT
    global sock, client
    
    TCP_IP = '172.30.1.31' # server socket`s IP
    TCP_PORT = 20000       # server socket`s PORT

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket 
    sock.bind((TCP_IP, TCP_PORT)) # bind socket to IP, port
    sock.listen(1) # wait client
    client, addr = sock.accept() # accept client, client = clilent`s socket, addr = client`s address 

    return None

init()

while True:
    length = recvall(client,16) # read (socket, bytes), length = data`s size
    stringData = recvall(client, int(length)) # 이미지의 길이만큼 데이터를 읽음
    data = numpy.fromstring(stringData, dtype='uint8') # 문자열 자료형으로부터 unsinged int형으로 변환

    decimg=cv2.imdecode(data, cv2.CV_LOAD_IMAGE_COLOR) # decoding
    cv2.imshow('CCTV', decimg) # show image
    now = datetime.now()
    cv2.imwrite('C:/list/' + now + '.jpg', decimg) # 이미지 저장 

sock.close()
# 사용자가 클릭해서 닫을 수 있도록 하자
'''
while True: # esc를 누를 때 까지 대기
    k = cv2.waitKey(0) 
    if k == 27:
        cv2.destroyAllWindows()
        break;
'''
