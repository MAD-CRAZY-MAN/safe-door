import socket
host = '172.30.1.27'
port = 20000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('created')

server_socket.bind((host, port))
print('binded')

server_socket.listen(1)
client_socket, addr = server_socket.accept()
print('connect')

data = client_socket.recv(65545)
print("recieve Data: ", data.decode())
