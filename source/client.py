import socket
from picamera import PiCamera
from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0', 9600) #serial init
camera = PiCamera()	                   #camera init

host = '172.30.1.27'
port = 20000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #server socket init
print('connect... ')
sock.connect((host, port)) #connect server socket
print('complte!')

while 1:
	response = ser.read() #read data from arduino
	if response == '1':
		camera.start_preview()
		sleep(2)
		camera.capture('/home/pi/Desktop/image.jpg')
		camera.stop_preview()
		sock.send("found thief".encode()) #send warning to server socket
		break
sock.close() #close server socket
