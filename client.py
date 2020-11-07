import socket

s = socket.socket()
host = "192.168.1.104"
port = 80
s.connect((host,port))
s.send('randomData'.encode())
data = ''
data = s.recv(1024).decode()
print (data)
s.close
