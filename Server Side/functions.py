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
        print("Tabela ja existe")

    sql = """
    CREATE TABLE aluno (
        aluno_id integer primary key autoincrement not null,
        nome text not null,
        idade integer not null
        );
    """
    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
    except:
        print("Tabela ja existe")

    
    sql = """
    CREATE TABLE prof (
        prof_id integer primary key autoincrement not null,
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
        print("Tabela ja existe")
    
    
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
        print("Tabela ja existe")
    
    sql = """
    CREATE TABLE disciplina_aluno(
        aluno_id integer not null,
        disciplina_id integer not null,
        FOREIGN KEY (aluno_id) REFERENCES aluno(aluno_id)
        );
    """

    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
        
    except:
        print("Tabela ja existe")
    
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
    except:
        print("Houve um erro")
    
    
    try:
        sql = """
        DELETE FROM disciplina_aluno
        WHERE disciplina_id = (?)
        """ 
        
        c = db_conn.cursor()
        
        c.execute(sql, (disciplina_id, ))
    except:
        print("Houve um erro")
    
    
    try:
        sql = """
        DELETE FROM disciplina
        WHERE disciplina_id = (?)
        """ 
        
        c = db_conn.cursor()
        
        c.execute(sql, (disciplina_id, ))
    except:
        print("Houve um erro")
