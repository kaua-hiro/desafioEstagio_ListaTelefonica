import sqlite3

# Cria o banco de dados e a tabela
def conectar():
    return sqlite3.connect("banco.db")
