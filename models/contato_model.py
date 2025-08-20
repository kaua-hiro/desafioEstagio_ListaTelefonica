# models/contato_model.py

import sqlite3

def criar_tabela():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lista_contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            numero_telefone TEXT NOT NULL,
            owner_id INTEGER NOT NULL,
            FOREIGN KEY (owner_id) REFERENCES usuarios (id)
        )
    """)
    conn.commit()
    conn.close()

def inserir_contato(db: sqlite3.Connection, nome: str, numero_telefone: str, owner_id: int) -> int:
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO lista_contatos (nome, numero_telefone, owner_id) VALUES (?, ?, ?)",
        (nome, numero_telefone, owner_id)
    )
    db.commit()
    return cursor.lastrowid

# MUDANÇA AQUI
def listar_contatos(db: sqlite3.Connection, owner_id: int, skip: int = 0, limit: int = 100, search: str | None = None) -> list:
    cursor = db.cursor()
    
    query = "SELECT id, nome, numero_telefone FROM lista_contatos WHERE owner_id = ?"
    params = [owner_id]

    if search:
        query += " AND nome LIKE ?"
        params.append(f"%{search}%")

    query += " LIMIT ? OFFSET ?"
    params.extend([limit, skip])
    
    cursor.execute(query, tuple(params))
    lista_contatos = cursor.fetchall()
    
    return [
        {"id": contato[0], "nome": contato[1], "numero_telefone": contato[2]}
        for contato in lista_contatos
    ]

def buscar_contato_por_id(db: sqlite3.Connection, contato_id: int, owner_id: int) -> dict | None:
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, numero_telefone FROM lista_contatos WHERE id = ? AND owner_id = ?", (contato_id, owner_id))
    contato = cursor.fetchone()

    if contato:
        return {"id": contato[0], "nome": contato[1], "numero_telefone": contato[2]}
    return None

def excluir_contatos(db: sqlite3.Connection, contato_id: int, owner_id: int) -> bool:
    cursor = db.cursor()
    cursor.execute("DELETE FROM lista_contatos WHERE id = ? AND owner_id = ?", (contato_id, owner_id))
    campos_afetados = cursor.rowcount
    db.commit()
    return campos_afetados > 0

def atualizar_contatos(db: sqlite3.Connection, contato_id: int, nome: str, numero_telefone: str, owner_id: int) -> bool:
    cursor = db.cursor()
    cursor.execute(
        "UPDATE lista_contatos SET nome = ?, numero_telefone = ? WHERE id = ? AND owner_id = ?",
        (nome, numero_telefone, contato_id, owner_id)
    )
    campos_afetados = cursor.rowcount
    db.commit()
    return campos_afetados > 0