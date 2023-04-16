import socket
import pickle

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
        
        s.sendall(escolha.encode())
        
        if "0" in escolha:
            quit()
        
        if escolha == "1":
            disciplina_nome = input("Nome da Disciplina -> ")
            s.sendall(disciplina_nome.encode())
            data = s.recv(1024)
            print(f"Server -> '{data.decode()}'")

        if escolha == "2":
            lista_disciplinas = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas as disciplinas exibidas!":
                    break
                lista_disciplinas.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_disciplinas:
                print(f"{i}")

        if escolha == "3":
            lista_disciplinas = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas as disciplinas exibidas!":
                    break
                lista_disciplinas.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_disciplinas:
                print(f"{i}")
            
            id_disciplina_a_apagar = input("Insira o ID da disciplina (0 para cancelar) ->")
            if id_disciplina_a_apagar == "0":
                pass
            else:
                s.sendall(id_disciplina_a_apagar.encode())
                data = s.recv(1024)
                print(f"Server -> '{data.decode()}'")
        
        if escolha == "4":
            nome_aluno = input("Nome do Aluno -> ")
            s.sendall(nome_aluno.encode())
            idade_aluno = input("Idade do Aluno -> ")
            s.sendall(idade_aluno.encode())
            aluno_id = input("ID do Aluno -> ")
            s.sendall(aluno_id.encode())
            morada = input("Morada Do Aluno -> ")
            s.sendall(morada.encode())
            data = s.recv(1024)
            print(f"{data.decode()}")

        if escolha == "5":
            lista_disciplinas = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas as disciplinas exibidas!":
                    break
                lista_disciplinas.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_disciplinas:
                print(f"{i}")
            id_disciplina = input("Insira o ID da disciplina que deseja associar a um aluno (0 para cancelar) ->")
            if id_disciplina == "0":
                pass
            else:
                s.send(id_disciplina.encode())
            

            lista_alunos = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas os Alunos exibidos!":
                    break
                lista_alunos.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_alunos:
                print(f"{i}")

            id_aluno = input("Insira o ID do aluno que deseja associar a uma disciplina (0 para cancelar) ->")
            if id_aluno == "0":
                pass
            else:
                s.send(id_aluno.encode())
            data = s.recv(1024)
            data = data.decode()
            print(f"{data}")
            pass

        if escolha == "6":

            lista_alunos = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas os Alunos exibidos!":
                    break
                lista_alunos.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_alunos:
                print(f"{i}")

            id_aluno = input("Insira o ID do aluno que deseja eliminar (0 para cancelar) ->")
            if id_aluno == "0":
                pass
            else:
                s.send(id_aluno.encode())
            data = s.recv(1024)
            data = data.decode()
            print(f"{data}")

            pass

        if escolha == "7":
            lista_alunos = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas os Alunos exibidos!":
                    break
                lista_alunos.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_alunos:
                print(f"{i}")
            
            pass
        pass
        
        if escolha == "8":
            lista_disciplinas = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas as disciplinas exibidas!":
                    break
                lista_disciplinas.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_disciplinas:
                print(f"{i}")
            id_disciplina = input("Insira o ID da disciplina que deseja ver os alunos associados (0 para cancelar) ->")
            if id_disciplina == "0":
                pass
            else:
                s.send(id_disciplina.encode())

            lista_alunos = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas os Alunos exibidos!":
                    break
                lista_alunos.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())
            
            for i in lista_alunos:
                print(f"{i}")