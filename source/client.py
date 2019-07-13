# 함수 화 하기, 이미지 저장(시간)
import socket
import cv2
import numpy
import serial

def init():
    global TCP_IP, TCP_PORT
    global sock, ser
    global encode_param, capture
    
    TCP_IP = '172.30.1.31' # server socket`s IP
    TCP_PORT = 5001        # server socket's PORT

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket, IP4v
    sock.connect((TCP_IP, TCP_PORT)) # connect socket

    ser = serial.Serial('/dev/ttyACM0', 9600) # serial connect

    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90] # encode jpg, img quality value
    capture = cv2.VideoCapture(0) # Create Video object No. 0 index

    return None

init()

while True:
    response = ser.read(1) # read data from arduino
    if response = '1':
        ret, frame = capture.read() # read 1 frame, return : True or Faluse, read frame
        result, imgencode = cv2.imencode('.jpg', frame, encode_param) # incode to jpg, at frame, above special type

        data = numpy.array(imgencode) # 배열을 만듬
        stringData = data.tostring() # 자료형을 문자열로 변환

        sock.send( str(len(stringData)).ljust(16)) # 읽은 데이터의 길이를 스트링으로 변환하고 16바이트에서 왼쪽 정렬
        sock.send( stringData ) # send an encodeing image to socket


sock.close() # close socket

'''
decimg=cv2.imdecode(data,1)
cv2.imshow('CLIENT',decimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
'''
