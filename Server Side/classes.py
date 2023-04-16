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


class Prof:

    def __init__(self, nome: str, idade: int, morada: str, cat: str, anos_exp: int):
        self.nome = nome
        self.idade = idade
        self.morada = morada
        self.categoria_pro = cat
        self.anos_exp = anos_exp
        self.disciplina = list()

    pass


class Disciplina:

    def __init__(self, nome: str):
        self.nome = nome

    pass
