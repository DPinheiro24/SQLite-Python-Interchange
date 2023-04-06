#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:28:24 2023

"""

import socket

HOST = "192.168.1.31"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(f"{data.decode()}")
            if not data:
                break
            str = "I hear you"
            conn.sendall(str.encode())
    
        


