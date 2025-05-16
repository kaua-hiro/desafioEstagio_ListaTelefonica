from database.db import conectar

def criar_tabela():
    conn = conectar()
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

def inserir_contato(nome: str, numero_telefone:str)-> int:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lista_contatos (nome, numero_telefone) "
    "VALUES (?, ?)", (nome, numero_telefone))
    conn.commit()

    last_id = cursor.lastrowid
    conn.close()
    return last_id

def listar_contatos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lista_contatos")
    lista_contatos = cursor.fetchall()
    conn.close()
    return [
        {
            "id": contato[0],
            "nome": contato[1],
            "numero_telefone": contato[2]
        }
        for contato in lista_contatos
    ]

def excluir_contatos(contato_id) -> bool:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lista_contatos WHERE id = ?", (contato_id,))

    campos_afetados = cursor.rowcount
    conn.commit()
    conn.close()
    return campos_afetados > 0

def buscar_contatos_por_id(contato_id) -> dict:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lista_contatos WHERE id = ?", (contato_id,))

    contato = cursor.fetchone()
    conn.close()
    return {
        "id": contato[0],
        "nome": contato[1],
        "numero_telefone": contato[2]
    } if contato else None

def atualizar_contatos(contato_id: int, nome: str, numero_telefone:str) -> bool:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE lista_contatos SET nome = ?, numero_telefone = ? "
    "WHERE id = ?", (nome, numero_telefone, contato_id))
    campos_afetados = cursor.rowcount
    conn.commit()
    conn.close()
    return campos_afetados > 0

