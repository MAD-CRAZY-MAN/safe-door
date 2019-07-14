import socket
import cv2
import numpy
import serial

TCP_IP = '172.30.1.31'
TCP_PORT = 5001

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

ser = serial.Serial('/dev/ttyACM0', 9600)

capture = cv2.VideoCapture(0)

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

while True:
    response = ser.read(1)
    if response = '1'
        ret, frame = capture.read()
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()

        sock.send( str(len(stringData)).ljust(16))
        sock.send( stringData )
sock.close()

decimg=cv2.imdecode(data,1)
cv2.imshow('CLIENT',decimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
