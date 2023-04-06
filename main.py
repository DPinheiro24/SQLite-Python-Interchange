import socket

s = socket.socket()
s.connect(('192.168.1.30', 8000))
while True:
    str = input("S: ")
    s.send(str.encode())
    if(str == "Bye" or str == "bye"):
        break
    print("N:"),s.recv(1024).decode()
s.close()