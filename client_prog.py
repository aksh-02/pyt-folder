# client program
import socket

my_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.connect(("192.168.74.102",4444)) # this address is of the server

my_socket.send(b"this is client") # b to convert the data in bytes
data=my_socket.recv(2048)  # receive data from the server
print(data)

my_socket.close()

