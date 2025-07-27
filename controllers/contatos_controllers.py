import sqlite3
from fastapi import HTTPException
from models import user_model


def mostrar_contatos(db: sqlite3.Connection) -> list[dict]:
    try:
        return user_model.listar_contatos(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar contatos: {str(e)}")

def buscar_contatos_por_id(db: sqlite3.Connection, contato_id: int) -> dict:
    try:
        contato = user_model.buscar_contatos_por_id(db, contato_id)
        if contato is None:
            raise HTTPException(status_code=404, detail="Contato não encontrado")
        return contato
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contato: {str(e)}")

def cadastrar_contatos(db: sqlite3.Connection, nome: str, numero_telefone: str) -> dict:
    try:
        contato_id = user_model.inserir_contato(db, nome, numero_telefone)
        return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar contato: {str(e)}")

def excluir_contatos(db: sqlite3.Connection, contato_id: int) -> dict:
    try:
        if not user_model.excluir_contatos(db, contato_id):
             raise HTTPException(status_code=404, detail="Contato não encontrado")
        return {"message": "Usuário excluído com sucesso."}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir contato: {str(e)}")

def atualizar_contatos(db: sqlite3.Connection, contato_id: int, nome: str, numero_telefone: str) -> dict:
    try:
        if not user_model.atualizar_contatos(db, contato_id, nome, numero_telefone):
             raise HTTPException(status_code=404, detail="Contato não encontrado")
        return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar contato: {str(e)}")