import sqlite3
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from controllers import contatos_controllers
from database.db import get_db
class Contato(BaseModel):
    nome: str
    numero_telefone: str

router = APIRouter()

@router.get("/contatos")
def pagina_inicial(db: sqlite3.Connection = Depends(get_db)):
    return contatos_controllers.mostrar_contatos(db)

@router.get("/contatos/{contato_id}")
def contato_por_id(contato_id: int, db: sqlite3.Connection = Depends(get_db)):
    return contatos_controllers.buscar_contatos_por_id(db, contato_id)

@router.post("/contatos", status_code=201)
def cadastrar(contato: Contato, db: sqlite3.Connection = Depends(get_db)):
    return contatos_controllers.cadastrar_contatos(
        db, nome=contato.nome, numero_telefone=contato.numero_telefone
    )

@router.delete("/contatos/delete/{contato_id}")
def deletar(contato_id: int, db: sqlite3.Connection = Depends(get_db)):
    return contatos_controllers.excluir_contatos(db, contato_id)

@router.put("/contatos/update/{contato_id}")
def atualizar(contato_id: int, contato: Contato, db: sqlite3.Connection = Depends(get_db)):
    return contatos_controllers.atualizar_contatos(
        db, contato_id=contato_id, nome=contato.nome, numero_telefone=contato.numero_telefone
    )