import socket

s=socket.socket() #socket object

port=6341 #reserve port in computer

s.bind(('',port))#coming from other computer on network

print("I am server in listening mode...")
s.listen(5)

connection,addr=s.accept()
print("Connection from ",addr)

message = connection.recv(1024)
print(message)
connection.close()

input("Pause")
