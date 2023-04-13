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
        idade integer not null,
        disciplina text not null,
        FOREIGN KEY (disciplina) REFERENCES disciplina(disciplina_id)
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
        morada text not null,
        disciplina text not null,
        FOREIGN KEY (disciplina) REFERENCES disciplina(disciplina_id)
        );
    """

    try:
        db_conn.executescript(sql)
        db_conn.commit()
        
        
    except:
        print("Tabela ja existe")
    
    db_conn.close()    
    
    pass

def criar_disciplina_db():

    global db_conn
    nomebd = "miniprojeto.db"
    db_conn = sqlite3.connect(nomebd)

    sql = """
    INSERT INTO disciplina (nome)
    VALUES ( ? );
    """

    for disciplina in lista_disciplina:

        pass
