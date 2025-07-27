import sqlite3

def criar_tabela():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lista_contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            numero_telefone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def inserir_contato(db: sqlite3.Connection, nome: str, numero_telefone: str) -> int:
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO lista_contatos (nome, numero_telefone) VALUES (?, ?)",
        (nome, numero_telefone)
    )
    db.commit()
    return cursor.lastrowid

def listar_contatos(db: sqlite3.Connection) -> list:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lista_contatos")
    lista_contatos = cursor.fetchall()
    
    return [
        {"id": contato[0], "nome": contato[1], "numero_telefone": contato[2]}
        for contato in lista_contatos
    ]

def buscar_contatos_por_id(db: sqlite3.Connection, contato_id: int) -> dict | None:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lista_contatos WHERE id = ?", (contato_id,))
    contato = cursor.fetchone()

    if contato:
        return {"id": contato[0], "nome": contato[1], "numero_telefone": contato[2]}
    return None

def excluir_contatos(db: sqlite3.Connection, contato_id: int) -> bool:
    cursor = db.cursor()
    cursor.execute("DELETE FROM lista_contatos WHERE id = ?", (contato_id,))
    campos_afetados = cursor.rowcount
    db.commit()
    return campos_afetados > 0

def atualizar_contatos(db: sqlite3.Connection, contato_id: int, nome: str, numero_telefone: str) -> bool:
    cursor = db.cursor()
    cursor.execute(
        "UPDATE lista_contatos SET nome = ?, numero_telefone = ? WHERE id = ?",
        (nome, numero_telefone, contato_id)
    )
    campos_afetados = cursor.rowcount
    db.commit()
    return campos_afetados > 0