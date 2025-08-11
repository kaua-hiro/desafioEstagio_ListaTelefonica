# routes/rotas.py

import sqlite3
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List

from controllers import contatos_controllers
from database.db import get_db
from routes.auth_routes import get_current_active_user
from schemas import user_schema

class Contato(BaseModel):
    nome: str
    numero_telefone: str

class ContatoResponse(Contato):
    id: int

router = APIRouter(
    prefix="/contatos",
    tags=["Contatos"],
    responses={404: {"description": "Não encontrado"}},
)

@router.get("/", response_model=List[ContatoResponse])
def pagina_inicial(db: sqlite3.Connection = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_active_user)):
    return contatos_controllers.mostrar_contatos(db, current_user_id=current_user["id"])

@router.get("/{contato_id}", response_model=ContatoResponse)
def contato_por_id(contato_id: int, db: sqlite3.Connection = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_active_user)):
    return contatos_controllers.buscar_contatos_por_id(db, contato_id, current_user_id=current_user["id"])

@router.post("/", status_code=201, response_model=ContatoResponse)
def cadastrar(contato: Contato, db: sqlite3.Connection = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_active_user)):
    return contatos_controllers.cadastrar_contatos(
        db, nome=contato.nome, numero_telefone=contato.numero_telefone, current_user_id=current_user["id"]
    )

@router.delete("/delete/{contato_id}")
def deletar(contato_id: int, db: sqlite3.Connection = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_active_user)):
    return contatos_controllers.excluir_contatos(db, contato_id, current_user_id=current_user["id"])

@router.put("/update/{contato_id}", response_model=ContatoResponse)
def atualizar(contato_id: int, contato: Contato, db: sqlite3.Connection = Depends(get_db), current_user: user_schema.UserResponse = Depends(get_current_active_user)):
    return contatos_controllers.atualizar_contatos(
        db, contato_id=contato_id, nome=contato.nome, numero_telefone=contato.numero_telefone, current_user_id=current_user["id"]
    )