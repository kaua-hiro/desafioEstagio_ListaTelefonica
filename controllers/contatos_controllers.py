# controllers/contatos_controllers.py

import sqlite3
from fastapi import HTTPException
from models import contato_model

# MUDANÇA AQUI
def mostrar_contatos(db: sqlite3.Connection, current_user_id: int, skip: int, limit: int, search: str | None) -> list[dict]:
    try:
        return contato_model.listar_contatos(db, owner_id=current_user_id, skip=skip, limit=limit, search=search)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar contatos: {str(e)}")

def buscar_contatos_por_id(db: sqlite3.Connection, contato_id: int, current_user_id: int) -> dict:
    try:
        contato = contato_model.buscar_contatos_por_id(db, contato_id, owner_id=current_user_id)
        if contato is None:
            raise HTTPException(status_code=404, detail="Contato não encontrado")
        return contato
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contato: {str(e)}")

def cadastrar_contatos(db: sqlite3.Connection, nome: str, numero_telefone: str, current_user_id: int) -> dict:
    try:
        contato_id = contato_model.inserir_contato(db, nome, numero_telefone, owner_id=current_user_id)
        return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar contato: {str(e)}")

def excluir_contatos(db: sqlite3.Connection, contato_id: int, current_user_id: int) -> dict:
    try:
        if not contato_model.excluir_contatos(db, contato_id, owner_id=current_user_id):
             raise HTTPException(status_code=404, detail="Contato não encontrado")
        return {"message": "Usuário excluído com sucesso."}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir contato: {str(e)}")

def atualizar_contatos(db: sqlite3.Connection, contato_id: int, nome: str, numero_telefone: str, current_user_id: int) -> dict:
    try:
        if not contato_model.atualizar_contatos(db, contato_id, nome, numero_telefone, owner_id=current_user_id):
             raise HTTPException(status_code=404, detail="Contato não encontrado")
        return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar contato: {str(e)}")