#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:28:24 2023

"""

import socket
import functions as f
from sys import exit

HOST = "192.168.1.31" # IP do Servidor
PORT = 65432 # Port a ser usada

f.criar_bd() # Ao iniciar o programa ele vai criar a base de dados, se já estiver criada levanta exceção


def menu(client_order, conn): # Função que vai correr todos os pedidos de queries ao functions.py
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

    escolha = client_order # Escolha será o que o servidor receber do cliente

    if escolha == "1":
        data = conn.recv(1024) # Visto que ambos os códigos estão a correr ao mesmo tempo é como se estivessem a correr espelhados. Então quando o clinte fala o servidor tem de ouvir
        reply = data.decode() # A comunicação entre os dois está em bytes, algo que n pode ser lido, por isso temos de converter para a forma original com decode()
        print(f"Nome da Disciplina: {reply}")
        f.criar_disciplina_db(reply) # Chama a função criar_disciplina_db() para criar uma disciplina e inserir na database, só precisando de um nome, visto que o ID é dado autonamente
        str = "Disciplina criada!"
        conn.sendall(str.encode()) # Envia a mensagem de sucesso para o cliente
        pass
    elif escolha == "2":
        resultado = f.listar_disciplina_db() # Chama a função listar_disciplina_db() e guarda o seu resultado numa variável
        for i in resultado: # Por cada disciplina que tiver corre esta parte do código
            lever = "Empty" # Cria uma variável que tem uma string que vai ser inicializada ao início de cada loop
            string = f" ID: {i[0]} | Disciplina: {i[1]}" # Guarda o resultado de cada loop numa variável
            conn.sendall(string.encode()) # Que vai ser enviado para o cliente
            while lever == "Empty": # O servidor depois espera pela resposta do cliente que recebeu essa string
                data = conn.recv(1024)
                reply = data.decode()
                lever = reply
        print("Lista percorrida!") # Informação para o Admin que o código acabou de ver todas as disciplinas
        str = "Todas as disciplinas exibidas!" # E informa também o cliente que está a espera de uma resposta do servidor
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
        data = conn.recv(1024) # Segue o princípio da parte anterior, mas desta vez recebemos mais uma vez uma informação do cliente, o ID por apagar
        reply = data.decode()
        print(f"ID da Disciplina por eliminar: {reply}")
        if not reply.isdigit(): # Se o cliente enviar algo na string que não seja um número, o cliente é informado de tal
            str = "Insira um numero sff" # TODO: Aprimorar esta defesa contra SQL Injection. Se esta funcionar aplicar ao código todo, mas é melhor arranjar uma melhor maneira
            conn.sendall(str.encode())
            return
        resultado = f.eliminar_disciplina_bd(reply)
        conn.sendall(resultado.encode())
        pass
    elif escolha == "4":

        #Recebe o nome, idade, aluno_id e morada pelo cliente
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

        resultado = f.criar_aluno_db(aluno_id, nome, idade, morada) # Chama a função criar_aluno_db com os valores anteriores para criar e inserir um aluno na database
        if resultado == "Ja existe uma disciplina com esse nome": # Se a função enviar uma mensagem de erro envia para o user
            conn.send(resultado.encode())
        else: # Se não continua normalmente, enviado a mensagem de sucesso ao cliente com o Id e Nome do Aluno
            for i in resultado:
                string = f"Aluno ID: {i[0]} | Nome: {i[1]}"
                conn.sendall(string.encode())
            print("Lista percorrida!")
        pass
    elif escolha == "5":
        resultado = f.listar_disciplina_db() # Chama a função listar_disciplina_db que guarda todas as disciplinas que a database tem na variável
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
        resultado = f.listar_aluno_db() # Chama a função listar_aluno_db que guarda todas os alunos que a database tem na variável
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
        resultado = f.insere_disciplina_aluno(aluno_id, id_disciplina) # Chama a função insere_disciplina_aluno e envia uma mensagem de sucesso ou erro ao cliente
        conn.sendall(resultado.encode())
        pass
    elif escolha == "6":
        resultado = f.listar_aluno_db() # Chama a função listar_aluno_db que guarda todas os alunos que a database tem na variável
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
        resultado = f.listar_aluno_db() # Chama a função listar_aluno_db que guarda todas os alunos que a database tem na variável
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
        resultado = f.listar_disciplina_db() # Chama a função listar_disciplina_db que guarda todas as disciplinas que a database tem na variável
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
        resultado = f.listar_aluno_inscrito_db(disciplina_id)# Chama a função listar_aluno_inscrito_db que guarda todas os alunos que a database tem na variável que estão associados a disciplina que o cliente deu
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

            #Recebe o nome, idade, id, categoria e morada do cliente
            data = conn.recv(1024)
            data = data.decode()
            nome = data
        
            data = conn.recv(1024)
            data = data.decode()
            idade = data
        
            data = conn.recv(1024)
            data = data.decode()
            prof_id = data
            
            data = conn.recv(1024)
            data = data.decode()
            cat_prof = data
            
            data = conn.recv(1024)
            data = data.decode()
            morada = data
            
            resultado = f.criar_prof_db(prof_id, nome, idade, cat_prof, morada) # Chama a função criar_prof_db que usa as variáveis obtidas anteriormente
            if resultado == "Ja existe um Professor com esse nome": # Se receber a mensagem de erro da função não corre o resto do programa
                conn.send(resultado.encode())
            else: # Se não continua normalmente, dando ao cliente o ID, Nome e Categoria do professor criado 
                for i in resultado:
                    string = f"Prof ID: {i[0]} | Nome: {i[1]} | Categoria Profissional: {i[2]}"
                    conn.sendall(string.encode())
                print("Lista percorrida!") # Informa o Admin que percorreu a lista toda TODO: Adicionar esta informação aos outros
            
            pass
    elif escolha == "10":
        resultado = f.listar_disciplina_db() # Chama a função listar_disciplina_db que guarda todas as disciplinas que a database tem na variável
        for i in resultado:
            lever = "Empty"
            string = f" ID: {i[0]} | Nome: {i[1]}"
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
        resultado = f.listar_prof_db() # Chama a função listar_prof_db() que guarda todos os professores qua a database tem na varável
        for i in resultado:
            lever = "Empty"
            string = f" ID: {i[0]} | Nome: {i[1]} | Categoria Profissional: {i[2]}"
            conn.sendall(string.encode())
            while lever == "Empty":
                data = conn.recv(1024)
                reply = data.decode()
                lever = reply
        print("Lista percorrida!")
        str = "Todas os professores exibidos!"
        conn.sendall(str.encode())
        data = conn.recv(1024)
        prof_id = data.decode()
        resultado = f.insere_disciplina_prof(prof_id, disciplina_id)
        conn.sendall(resultado.encode())
        pass

    pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Abrevia o palavriado todo para não ter de escrever tudo 
    s.bind((HOST, PORT)) # "Vincula" o Servidor ao IP e a Port
    s.listen() # O servidor aceita comunicações
    while True: # O loop tem de ter dentro o s.accept() para estar sempre a aceitar pelo menos um cliente
        try:
            conn, addr = s.accept() # Aceita o servidor e guarda o IP do cliente e a port onde a conecção foi estabelecida
            with conn:
                print(f"Connected by {addr}") # Guarda para razões de administração esses valores
                while True: # Até o cliente digitar "0" o código vai continuar a espera de uma mensagem do usuário que será o 1-10 que relaciona com o menu
                    data = conn.recv(1024)
                    client_order = data.decode()
                    print(f"{client_order}") # Por razões de administração guarda o que o cliente pediu do servidor
                    if client_order == "0": # Se o cliente digitar "0" sai do loop. Como na parte do cliente digitar 0 faz com que o código termine, o servidor ficará disponível e voltará a esperar uma nova ligação
                        break
                    if client_order == "290803": # Este código é apenas conhecido a quem tem acesso ao servidor. Se o cliente digitar este código o servidor termina o programa como o cliente
                        conn.close()
                        exit()
                    menu(client_order, conn) # Chama a função menu() com a opção do cliente e a sua conexão
        except ConnectionResetError: # Se o cliente tentar terminar abrutamente a conexão, este try/except impede o servidor de fechar inesperadamente e voltar a espera de comunicações
            print("Conexao Terminada...")
    pass
