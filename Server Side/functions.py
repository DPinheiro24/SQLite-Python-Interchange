#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 18:15:48 2023

@author: formando
"""

import sqlite3


def criar_bd():
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql = """
    CREATE TABLE disciplina (
        disciplina_id integer primary key autoincrement not null,
        nome text not null
        );
    """
    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
        
    except:
        print("Tabela disciplina ja existe")

    sql = """
    CREATE TABLE aluno (
        aluno_id integer primary key not null,
        nome text not null,
        idade integer not null,
        morada text not null
        );
    """
    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
    except:
        print("Tabela aluno ja existe")

    
    sql = """
    CREATE TABLE prof (
        prof_id integer primary key not null,
        nome text not null,
        idade integer not null,
        cat_profissional text not null,
        morada text not null
        );
    """

    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
        
    except:
        print("Tabela prof ja existe")
    
    
    sql = """
    CREATE TABLE disciplina_prof(
        prof_id integer not null,
        disciplina_id integer not null,
        FOREIGN KEY (prof_id) REFERENCES prof(prof_id)
        FOREIGN KEY (disciplina_id) REFERENCES disciplina(disciplina_id)
        );
    """

    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
        
    except:
        print("Tabela disciplina_prof ja existe")
    
    sql = """
    CREATE TABLE disciplina_aluno(
        aluno_id integer not null,
        disciplina_id integer not null,
        FOREIGN KEY (aluno_id) REFERENCES aluno(aluno_id)
        FOREIGN KEY (disciplina_id) REFERENCES disciplina(disciplina_id)
        );
    """

    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
        
    except:
        print("Tabela disciplina_aluno ja existe")
    
    db_conn.close()    
    
    pass

def criar_disciplina_db(nome):

    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)

    sql = """
    INSERT INTO disciplina (nome)
    VALUES (?);
    """
    
    c = db_conn.cursor()
    
    c.execute(sql, (nome,))
    db_conn.commit()
    pass

def criar_aluno_db(aluno_id, nome, idade, morada):
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)

    sql = """
    INSERT INTO aluno (aluno_id, nome, idade, morada)
    VALUES (?,?,?,?);
    """
    
    c = db_conn.cursor()
    
    c.execute(sql, (aluno_id, nome, idade, morada, ))
    db_conn.commit()
    
    sql = """
    SELECT aluno_id, nome FROM aluno WHERE aluno_id = (?) LIMIT 1;
    """   
    
    c.execute(sql, (aluno_id, ))
    resultado = c.fetchall()
    return resultado
    
    pass

def listar_disciplina_db():
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql = """
    SELECT disciplina_id, nome FROM disciplina;
    """    
    
    c = db_conn.cursor()    
    c.execute(sql)
    resultado = c.fetchall()
    return resultado
    
def listar_aluno_db():
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql = """
    SELECT aluno_id, nome FROM aluno;
    """    
    
    c = db_conn.cursor()    
    c.execute(sql)
    resultado = c.fetchall()
    return resultado


def eliminar_disciplina_bd(disciplina_id):
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    try:
        sql = """
        DELETE FROM disciplina_prof
        WHERE disciplina_id = (?)
        """ 
        
        c = db_conn.cursor()
        
        c.execute(sql, (disciplina_id, ))
        db_conn.commit()
    except:
        print("Houve um erro em 1, nao deve haver esse ID aqui")
    
    
    try:
        sql = """
        DELETE FROM disciplina_aluno
        WHERE disciplina_id = (?)
        """ 
        
        c = db_conn.cursor()
        
        c.execute(sql, (disciplina_id, ))
        db_conn.commit()
    except:
        print("Houve um erro em 2, nao deve haver esse ID aqui")
    
    
    try:
        sql = """
        DELETE FROM disciplina
        WHERE disciplina_id = (?)
        """ 
        
        c = db_conn.cursor()
        
        c.execute(sql, (disciplina_id, ))
        db_conn.commit()
        print(f"ID {disciplina_id} foi apagado com sucesso!")
        str = f"ID {disciplina_id} foi apagado com sucesso!"
        return str
    except:
        print("Houve um erro em 3, o ID nao existe")
        str = "Houve um erro, o ID nao existe"
        return str


def insere_disciplina_aluno(aluno_id, disciplina_id):
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql="""
    INSERT INTO disciplina_aluno (aluno_id, disciplina_id)
    VALUES (?,?);
    
    """
    
    try:
        c = db_conn.cursor()
        
        c.execute(sql, (aluno_id, disciplina_id, ))
        db_conn.commit()
        str = "Aluno associado com sucesso"
        return str
    except:
        str = "Aconteceu um erro, tem a certeza que tem os IDs corretos?"
        return str