# models/user_model.py

import sqlite3
from schemas import user_schema
from utils.security import gerar_hash_senha

def criar_tabela_usuarios():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def criar_usuario(db: sqlite3.Connection, usuario: user_schema.UserCreate):
    senha_hasheada = gerar_hash_senha(usuario.password)
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO usuarios (email, senha_hash) VALUES (?, ?)",
        (usuario.email, senha_hasheada)
    )
    db.commit()
    novo_usuario_id = cursor.lastrowid
    return {"id": novo_usuario_id, **usuario.dict()}

def buscar_usuario_por_email(db: sqlite3.Connection, email: str):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()
    if usuario:
        return {"id": usuario[0], "email": usuario[1], "senha_hash": usuario[2]}
    return None