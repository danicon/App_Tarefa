# importando sqlite3
import sqlite3 as lite
from sqlite3.dbapi2 import Cursor

# criando BD
con = lite.connect("lista.db")

def inserir(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tarefa (nome) VALUES (?) "
        cur.execute(query, i)
        
def selecionar():
    lista_tarefa = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa ")
        row = cur.fetchall()
        for r in row:
            lista_tarefa.append(r)
    return lista_tarefa

def deletar(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM tarefa WHERE id=? "
        cur.execute(query, i)

def atualizar(i):
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET nome='Comer' WHERE id=3 "
        cur.execute(query, i)    




'''
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tarefa (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

'''