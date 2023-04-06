#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:18:19 2023

@author: formando
"""

import cv2
import pytesseract
from tkinter import filedialog
import sqlite3

while (escolha != 0 ):
    
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
    
    escolha = int(input("Insira a opçao que deseja -> "))
    
    if escolha == 1:
        criar_disciplina()
    elif escolha == 2:
        listar_disciplinas()
    elif escolha == 3:
        eliminar_disciplina()
    elif escolha == 4:
        criar_aluno()
    elif escolha == 5:
        inscrever_aluno()
    elif escolha == 6:
        delete_aluno()
    elif escolha == 7:
        listar_aluno()
    elif escolha == 8:
        listar_aluno_disc()
    elif escolha == 9:
        criar_professor()
    elif escolha == 10:
        assign_professor()
    
    pass
