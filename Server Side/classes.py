#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:30:36 2023

@author: formando
"""

class Aluno:
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.disciplina = list()
    
    def listar_informacoes(self):
        counter = 1
        
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        for i in self.disciplina:
            print(f"Disciplina {counter}: {i}")
            counter += 1
        
    pass
        
class Prof(Aluno):
    
    

    pass        
        
        
