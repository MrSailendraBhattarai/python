import socket

s=socket.socket()

port=6341

ip='192.168.1.143'

s.connect((ip,port))

print("Connected to Server...")

s.send(b"Hello I am Sailendra ")

s.close

input("pause")