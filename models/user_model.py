from database.db import conectar

# models/user_model.py
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


# Inserir um novo usuário
def inserir_contato(nome: str, numero_telefone:str)-> int:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lista_contatos (nome, numero_telefone) "
    "VALUES (?, ?)", (nome, numero_telefone))
    conn.commit()
    #lastrowid retorna o id do último registro inserido
    # Isso é útil para saber qual ID foi atribuído ao novo contato
    last_id = cursor.lastrowid
    conn.close()
    return last_id

# Função para listar todos os usuários
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

# Função para excluir um usuário
def excluir_contatos(contato_id) -> bool:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lista_contatos WHERE id = ?", (contato_id,))
    #rowcount retorna o número de linhas afetadas pela última operação
    # Se rowcount for maior que 0, significa que a exclusão foi bem-sucedida
    campos_afetados = cursor.rowcount
    conn.commit()
    conn.close()
    return campos_afetados > 0

# Função para buscar um usuário por ID
def buscar_contatos_por_id(contato_id) -> dict:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lista_contatos WHERE id = ?", (contato_id,))
#FETCHONE retorna apenas uma linha
#FETCHALL retorna todas as linhas
#FETCHMANY retorna um número específico de linhas 
    contato = cursor.fetchone()
    conn.close()
    return {
        "id": contato[0],
        "nome": contato[1],
        "numero_telefone": contato[2]
    } if contato else None

# Função para atualizar um usuário
def atualizar_contatos(contato_id: int, nome: str, numero_telefone:str) -> bool:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE lista_contatos SET nome = ?, numero_telefone = ? "
    "WHERE id = ?", (nome, numero_telefone, contato_id))
    campos_afetados = cursor.rowcount
    conn.commit()
    conn.close()
    return campos_afetados > 0

