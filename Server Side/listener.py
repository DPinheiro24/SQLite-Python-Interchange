#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:28:24 2023

"""

import socket
import sqlite3
import functions as f
from sys import exit
import pickle

HOST = "192.168.1.31"  
PORT = 65432  

f.criar_bd()

def menu(client_order, conn):
        '''
        print("******** MENU ********")
        print("1 - Criar Disciplina")
        print("2 - Listar Disciplinas")
        print("3 - Eliminar Disciplina")
        print("4 - Criar Aluno")
        print("5 - Inscrever Aluno")
        print("6 - Eliminar Aluno")
        print("7 - Listar Alunos")
        print("8 - Listar Alunos inscritos numa dada disciplina")
        print("9 - Criar Professor")
        print("10 - Adicionar professor a uma disciplina")
        print("0 - Sair")
        print("***********************")
        '''
        
        escolha = client_order
        
        if escolha == "1":
            data = conn.recv(1024)
            reply = data.decode()
            print(f"Nome da Disciplina: {reply}")
            f.criar_disciplina_db(reply)
            str = "Disciplina criada!"
            conn.sendall(str.encode())
            pass
        elif escolha == "2":
            resultado = f.listar_disciplina_db()
            for i in resultado:
                string = f" ID: {i[0]} | Disciplina: {i[1]}"
                conn.sendall(string.encode())
            print("Lista percorrida!")
            str = "Todas as disciplinas exibidas!"
            conn.sendall(str.encode())
            pass
        elif escolha == "3":
            data = conn.recv(1024)
            reply = data.decode()
            print(f"ID da Disciplina por eliminar: {reply}")
            if not reply.isdigit():
                    str = "Insira um numero sff" 
                    return
            f.eliminar_disciplina_bd(reply)
            pass
        elif escolha == "4":
            #criar_aluno()
            pass
        elif escolha == "5":
            #inscrever_aluno()
            pass
        elif escolha == "6":
            #delete_aluno()
            pass
        elif escolha == "7":
            #listar_aluno()
            pass
        elif escolha == "8":
            #listar_aluno_disc()
            pass
        elif escolha == "9":
            #criar_professor()
            pass
        elif escolha == "10":
            #assign_professor()
            pass
        
        pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                client_order = data.decode()
                print(f"{client_order}")
                if client_order == "0":
                    break
                if client_order == "290803":
                    exit()
                menu(client_order, conn)
    
