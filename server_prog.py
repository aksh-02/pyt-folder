# server program
import socket

# below the first parameter is socket_family, the 2nd is socket_type and the third which ahs been left out is protocol
my_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get local machine name
#host=socket.gethostname()
 
my_socket.bind(("192.168.74.102",4444)) #  binds address (hostname, port number) to socket

my_socket.listen(5)

conn,address=my_socket.accept() # conn is a socket object and address is an (ip,port) pair on the client side

data=conn.recv(2048)
print(data)

conn.send("This is server".encode('utf-8')) # encode('utf-8 ') to concert the data in bytes

my_socket.close()  # closes the socket


