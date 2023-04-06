import socket

HOST = "192.168.1.31"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    str = input("S: ")
    s.sendall(str.encode())
    data = s.recv(1024)

print(f"Received '{data.decode()}'")