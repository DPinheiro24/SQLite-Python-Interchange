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
    
    sql="""
    SELECT COUNT(*) FROM disciplina WHERE nome = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (nome, ))
    conta = c.fetchall()
    if len(conta) >= 1:
        print("Ha alguem aqui! Disciplina ja existe")
        return "Ja existe uma disciplina com esse nome"
    else:
        print("Nao ha ninguem aqui!")

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
    
    sql="""
    SELECT COUNT(*) FROM aluno WHERE nome = (?);
    """
    
    c = db_conn.cursor()
    c.execute(sql, (nome, ))
    conta = c.fetchall()
    extra = 0
    for i in conta:
        for x in i:
            extra = x
    if extra >= 1:
        print("Ha alguem aqui! Aluno ja existe")
        return "Ja existe uma disciplina com esse nome"
    else:
        print("Nao ha ninguem aqui!")
    
    try:
        sql = """
        INSERT INTO aluno (aluno_id, nome, idade, morada)
        VALUES (?,?,?,?);
        """
        
        c = db_conn.cursor()
        
        c.execute(sql, (aluno_id, nome, idade, morada, ))
        db_conn.commit()
    except Exception as e:
        print(f"Houve um erro ao criar o aluno: {str(e)}")
        return "Ocorreu um erro"
    
    sql = """
    SELECT aluno_id, nome FROM aluno WHERE aluno_id = (?) LIMIT 1;
    """   
    
    c.execute(sql, (aluno_id, ))
    resultado = c.fetchall()
    return resultado
    
    pass

def criar_prof_db(prof_id, nome, idade, cat_profissional, morada):
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql="""
    SELECT COUNT(*) FROM prof WHERE nome = (?);
    """
    
    c = db_conn.cursor()
    c.execute(sql, (nome, ))
    conta = c.fetchall()
    extra = 0
    for i in conta:
        for x in i:
            extra = x
    if extra >= 1:
        print("Ha alguem aqui! Professor ja existe")
        return "Ja existe um Professor com esse nome"
    else:
        print("Nao ha ninguem aqui!")
    
    try:
        sql = """
        INSERT INTO prof (prof_id, nome, idade, cat_profissional, morada)
        VALUES (?,?,?,?,?);
        """
        
        c = db_conn.cursor()
        
        c.execute(sql, (prof_id, nome, idade, cat_profissional, morada, ))
        db_conn.commit()
    except Exception as e:
        print(f"Houve um erro ao criar o professor: {str(e)}")
        return "Ocorreu um erro"
    
    sql = """
    SELECT prof_id, nome, cat_profissional FROM prof WHERE prof_id = (?) LIMIT 1;
    """   
    
    c.execute(sql, (prof_id, ))
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

def listar_prof_db():
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql = """
    SELECT prof_id, nome, cat_profissional FROM prof;
    """    
    
    c = db_conn.cursor()    
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

def listar_aluno_inscrito_db(disciplina):
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql = """
    SELECT aluno.aluno_id, aluno.nome FROM aluno 
    JOIN disciplina_aluno ON disciplina_aluno.aluno_id = aluno.aluno_id
    WHERE disciplina_aluno.disciplina_id = (?);
    """    
    
    c = db_conn.cursor()    
    c.execute(sql, (disciplina, ))
    resultado = c.fetchall()
    return resultado

def eliminar_disciplina_bd(disciplina_id):
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql="""
    SELECT COUNT(*) FROM disciplina WHERE disciplina_id = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (disciplina_id, ))
    conta = c.fetchall()
    if len(conta) == 1:
        print("Ha alguem aqui!")
    elif len(conta) >= 1:
        print("Ha mais que um??")
    else:
        print("Nao ha ninguem aqui!")
        return "Database Vazia"
    
    
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
        db_conn.close()
    
    
    try:
        sql = """
        DELETE FROM disciplina
        WHERE disciplina_id = (?)
        """ 
        
        c = db_conn.cursor()
        
        c.execute(sql, (disciplina_id, ))
        db_conn.commit()
        db_conn.close()
        print(f"ID {disciplina_id} foi apagado com sucesso!")
        str = f"ID {disciplina_id} foi apagado com sucesso!"
        return str
    except Exception as e:
        print(f"Houve um erro ao apagar a disciplina: {str(e)}")
        db_conn.close()
        return "Houve um erro, o ID nao existe"
    
    
def eliminar_aluno_bd(aluno_id):
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql="""
    SELECT COUNT(*) FROM aluno WHERE aluno_id = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (aluno_id, ))
    conta = c.fetchall()
    if len(conta) == 1:
        print("Ha alguem aqui!")
    elif len(conta) >= 1:
        print("Ha mais que um??")
    else:
        print("Nao ha ninguem aqui!")
        return "Database Vazia"
    
    
    try:
        sql = """
        DELETE FROM disciplina_aluno
        WHERE aluno_id = (?)
        """ 
        c = db_conn.cursor()
        c.execute(sql, (aluno_id,))
        if c.rowcount == 0:
            print(f"Erro: aluno com ID {aluno_id} não encontrado na tabela disciplina_aluno. O aluno pode nao ter sido associado a nenhuma disciplina.")

        sql = """
        DELETE FROM aluno
        WHERE aluno_id = (?)
        """ 
        c = db_conn.cursor()
        c.execute(sql, (aluno_id,))
        db_conn.commit()
        db_conn.close()
        print(f"ID {aluno_id} foi apagado com sucesso!")
        return f"ID {aluno_id} foi apagado com sucesso!"

    except Exception as e:
        db_conn.close()
        print(f"Houve um erro ao apagar o aluno: {str(e)}")
        return "Erro ao apagar aluno"

    

def insere_disciplina_aluno(aluno_id, disciplina_id):
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    
    sql="""
    SELECT nome FROM disciplina WHERE disciplina_id = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (disciplina_id, ))
    conta = c.fetchall()
    if c.rowcount == 0:
        db_conn.close()
        return "Disciplina nao existe"
    
    sql="""
    SELECT nome FROM aluno WHERE aluno_id = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (aluno_id, ))
    conta = c.fetchall()
    if c.rowcount == 0:
        db_conn.close()
        return "Aluno nao existe"
    
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

def insere_disciplina_prof(prof_id, disciplina_id):
    
    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)
    print(f"{prof_id} | {disciplina_id}")
    
    sql="""
    SELECT nome FROM disciplina WHERE disciplina_id = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (disciplina_id, ))
    conta = c.fetchall()
    if c.rowcount == 0:
        db_conn.close()
        return "Disciplina nao existe"
    
    sql="""
    SELECT nome FROM prof WHERE prof_id = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (prof_id, ))
    conta = c.fetchall()
    if c.rowcount == 0:
        db_conn.close()
        return "Professor nao existe"
    
    sql="""
    SELECT COUNT(*) FROM disciplina_prof WHERE prof_id = (?);
    """
    c = db_conn.cursor()
    c.execute(sql, (prof_id, ))
    conta = c.fetchall()
    extra = 0
    for i in conta:
        for x in i:
            extra = x
    if extra == 1:
        print("Ha alguem aqui!")
        return "Professor ja tem disciplina"
    else:
        print("Nao ha ninguem aqui!")
    
    
    sql="""
    INSERT INTO disciplina_prof (prof_id, disciplina_id)
    VALUES (?,?);
    
    """
    
    try:
        c = db_conn.cursor()
        
        c.execute(sql, (prof_id, disciplina_id, ))
        db_conn.commit()
        return "Professor associado com sucesso"
    except:
        
        return "Aconteceu um erro, tem a certeza que tem os IDs corretos?"
