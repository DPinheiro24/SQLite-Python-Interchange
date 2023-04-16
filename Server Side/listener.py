#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:28:24 2023

"""

import socket
import functions as f
from sys import exit

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
                lever = "Empty"
                string = f" ID: {i[0]} | Disciplina: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
            print("Lista percorrida!")
            str = "Todas as disciplinas exibidas!"
            conn.sendall(str.encode())
            pass
        elif escolha == "3":
            resultado = f.listar_disciplina_db()
            for i in resultado:
                lever = "Empty"
                string = f" ID: {i[0]} | Disciplina: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
            print("Lista percorrida!")
            str = "Todas as disciplinas exibidas!"
            conn.sendall(str.encode())
            data = conn.recv(1024)
            reply = data.decode()
            print(f"ID da Disciplina por eliminar: {reply}")
            if not reply.isdigit():
                    str = "Insira um numero sff"
                    conn.sendall(str.encode())
                    return
            resultado = f.eliminar_disciplina_bd(reply)
            conn.sendall(resultado.encode())
            pass
        elif escolha == "4":
            
            data = conn.recv(1024)
            data = data.decode()
            nome = data
        
            data = conn.recv(1024)
            data = data.decode()
            idade = data
        
            data = conn.recv(1024)
            data = data.decode()
            aluno_id = data
        
            data = conn.recv(1024)
            data = data.decode()
            morada = data
                
            resultado = f.criar_aluno_db(aluno_id, nome, idade, morada)
            if resultado == "Ja existe uma disciplina com esse nome":
                conn.send(resultado.encode())
            else:
                for i in resultado:
                    string = f"Aluno ID: {i[0]} | Nome: {i[1]}"
                    conn.sendall(string.encode())
                print("Lista percorrida!")
            pass
        elif escolha == "5":
            resultado = f.listar_disciplina_db()
            for i in resultado:
                lever = "Empty"
                string = f" ID: {i[0]} | Disciplina: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
                    print(f"{string} | {lever}")
            print("Lista percorrida!")
            str = "Todas as disciplinas exibidas!"
            conn.sendall(str.encode())
            data = conn.recv(1024)
            id_disciplina = data.decode()
            print(f"ID da Disciplina: {id_disciplina}")
            resultado = f.listar_aluno_db()
            for i in resultado:
                lever = "Empty"
                string = f" ID: {i[0]} | Nome: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
                    print(f"{string} | {lever}")
            print("Lista percorrida!")
            str = "Todas os Alunos exibidos!"
            conn.sendall(str.encode())
            data = conn.recv(1024)
            aluno_id = data.decode()
            print(f"ID do Aluno: {aluno_id}")
            resultado = f.insere_disciplina_aluno(aluno_id, id_disciplina)
            conn.sendall(resultado.encode())
            pass
        elif escolha == "6":
            resultado = f.listar_aluno_db()
            for i in resultado:
                lever = "Empty"
                string = f" ID: {i[0]} | Nome: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
                    print(f"{string} | {lever}")
            print("Lista percorrida!")
            str = "Todas os Alunos exibidos!"
            conn.sendall(str.encode())
            data = conn.recv(1024)
            reply = data.decode()
            print(f"ID do Aluno por eliminar: {reply}")
            resultado = f.eliminar_aluno_bd(reply)
            conn.sendall(resultado.encode())
            pass
        elif escolha == "7":
            resultado = f.listar_aluno_db()
            for i in resultado:
                lever = "Empty"
                string = f" ID: {i[0]} | Nome: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
            print("Lista percorrida!")
            str = "Todas os Alunos exibidos!"
            conn.sendall(str.encode())
            pass
        elif escolha == "8":
            resultado = f.listar_disciplina_db()
            for i in resultado:
                lever = "Empty"
                string = f" ID: {i[0]} | Disciplina: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
            print("Lista percorrida!")
            str = "Todas as disciplinas exibidas!"
            conn.sendall(str.encode())
            data = conn.recv(1024)
            disciplina_id = data.decode()
            resultado = f.listar_aluno_inscrito_db(disciplina_id)
            for i in resultado:
                lever = "Empty"
                string = f" ID: {i[0]} | Nome: {i[1]}"
                conn.sendall(string.encode())
                while lever == "Empty":
                    data = conn.recv(1024)
                    reply = data.decode()
                    lever = reply
            print("Lista percorrida!")
            str = "Todas os Alunos exibidos!"
            conn.sendall(str.encode())
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
        try:
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
        except ConnectionResetError:
            print("Conexao Terminada...")
    pass
