import socket
import pickle

HOST = "192.168.1.31" # IP do Server
PORT = 65432 # Port para ser usado

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Abrevia o palavriado todo para não ter de escrever tudo 
    s.connect((HOST, PORT)) # Conecta ao servidor, se não conseguir há um erro
    while True: # Corre o proograma até ser interrompido

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

        s.sendall(escolha.encode()) # Envia a escolha para o servidor em bytes

        if escolha == "1":
            disciplina_nome = input("Nome da Disciplina -> ")
            s.sendall(disciplina_nome.encode())
            data = s.recv(1024) # Recebe do servidor e reverte de bytes na linha a seguir
            print(f"Server -> '{data.decode()}'")
            pass

        if escolha == "2":
            lista_disciplinas = [] # Cria uma lista para guardar os resultados que vão ser enviados pelo servidor
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas as disciplinas exibidas!": # Até o servidor disser que enviou todas as disciplinas, o cliente vai ficar a ouvir e a receber informação
                    break
                lista_disciplinas.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())

            for i in lista_disciplinas: # Após toda a informação ter sido adicionada a lista, o código corre a lista e da print em todas as disciplinas dadas
                print(f"{i}")
            pass

        if escolha == "3":
            lista_disciplinas = [] # Cria uma lista para guardar os resultados que vão ser enviados pelo servidor
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas as disciplinas exibidas!": # Até o servidor disser que enviou todas as disciplinas, o cliente vai ficar a ouvir e a receber informação
                    break
                lista_disciplinas.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())

            for i in lista_disciplinas: # Após toda a informação ter sido adicionada a lista, o código corre a lista e da print em todas as disciplinas dadas
                print(f"{i}")

            id_disciplina_a_apagar = input(
                "Insira o ID da disciplina (0 para cancelar) ->")
            if id_disciplina_a_apagar == "0":
                pass # Se o cliente selecionar "0", o código ignora o resto e acaba esta parte. O "pass" é como um ";" no C, o programa entende que está lá mas não faz nada
            else:
                s.sendall(id_disciplina_a_apagar.encode())
                data = s.recv(1024)
                print(f"Server -> '{data.decode()}'") # Da print da informação que o Servidor dá, uma mensagem de erro ou uma de successo neste caso
            pass

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
            pass

        if escolha == "5":
            lista_disciplinas = [] # Cria uma lista para guardar os resultados que vão ser enviados pelo servidor
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas as disciplinas exibidas!": # Até o servidor disser que enviou todas as disciplinas, o cliente vai ficar a ouvir e a receber informação
                    break
                lista_disciplinas.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())

            for i in lista_disciplinas:
                print(f"{i}")
            id_disciplina = input(
                "Insira o ID da disciplina que deseja associar a um aluno (0 para cancelar) ->")
            if id_disciplina == "0": # Após toda a informação ter sido adicionada a lista, o código corre a lista e da print em todas as disciplinas dadas
                pass
            else:
                s.send(id_disciplina.encode())

            lista_alunos = [] # Segue o mesmo princípio que a das disciplinas, só muda o nome das váriaveis
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

            id_aluno = input(
                "Insira o ID do aluno que deseja associar a uma disciplina (0 para cancelar) ->")
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

            id_aluno = input(
                "Insira o ID do aluno que deseja eliminar (0 para cancelar) ->")
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
            id_disciplina = input(
                "Insira o ID da disciplina que deseja ver os alunos associados (0 para cancelar) ->")
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
            pass

        if escolha == "9":
            nome_prof = input("Nome do Professor -> ")
            s.sendall(nome_prof.encode())
            idade_prof = input("Idade do Professor -> ")
            s.sendall(idade_prof.encode())
            prof_id = input("ID do Professor -> ")
            s.sendall(prof_id.encode())
            cat_prof = input("Categoria Profissional do Professor -> ")
            s.sendall(cat_prof.encode())
            morada = input("Morada Do Professor -> ")
            s.sendall(morada.encode())
            data = s.recv(1024)
            print(f"{data.decode()}")
            pass

        if escolha == "10":
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
            id_disciplina = input(
                "Insira o ID da disciplina que deseja associar a um prof (0 para cancelar) ->")
            if id_disciplina == "0":
                pass
            else:
                s.send(id_disciplina.encode())

            lista_profs = []
            while True:
                data = s.recv(1024)
                data = data.decode()
                if data == "Todas os professores exibidos!":
                    break
                lista_profs.append(data)
                str = "Client -> Received!\n"
                s.sendall(str.encode())

            for i in lista_profs:
                print(f"{i}")
            id_prof = input(
                "Insira o ID do professor que quer associar(0 para cancelar) ->")
            if id_prof == "0":
                pass
            else:
                s.send(id_prof.encode())
            data = s.recv(1024)
            data = data.decode()
            print(f"Server -> {data}")
            pass
        elif "0" in escolha: # Se a escolha tiver 0 (sem ser 10, visto que está esta parte do código está num elif)
            quit()
