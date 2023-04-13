import socket

HOST = "192.168.1.31"  
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
    
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
        
        escolha = input("Insira a opçao que deseja -> ")
        
        if escolha == "1":
            s.sendall(escolha.encode())
        elif escolha == "2":
            s.sendall(escolha.encode())
        elif escolha == "3":
            s.sendall(escolha.encode())
        elif escolha == "4":
            s.sendall(escolha.encode())
        elif escolha == "5":
            s.sendall(escolha.encode())
        elif escolha == "6":
            s.sendall(escolha.encode())
        elif escolha == "7":
            s.sendall(escolha.encode())
        elif escolha == "8":
            s.sendall(escolha.encode())
        elif escolha == "9":
            s.sendall(escolha.encode())
        elif escolha == "10":
            s.sendall(escolha.encode())
        elif escolha == "0":
            s.sendall(escolha.encode())
            data = s.recv(1024)
            print(f"Received '{data.decode()}'")
            s.close()
            break
        else:
            s.sendall(escolha.encode())
        
        data = s.recv(1024)
        print(f"Received '{data.decode()}'")
    pass
