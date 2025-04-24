from fastapi import APIRouter, Request
from controllers import contatos_controllers
from pydantic import BaseModel
from typing import List

class Contato(BaseModel):
    nome: str
    numero_telefone: str
router = APIRouter()

# Rota inicial
@router.get("/contatos")
def pagina_inicial():
    return contatos_controllers.mostrar_contatos()

# Rota para mostrar todos os usuários
@router.get("/contatos/{contato_id}")
def contato_por_id(contato_id: int):
    return contatos_controllers.buscar_contatos_por_id(contato_id)   

# Rota para criar um novo usuário
@router.post("/contatos", status_code=201)
async def cadastrar(contato: Contato):
    return await contatos_controllers.cadastrar_contatos(nome=contato.nome, numero_telefone=contato.numero_telefone)

# Rota para excluir um usuário
@router.delete("/contatos/delete/{contato_id}")
def deletar(contato_id: int):
    return contatos_controllers.excluir_contatos(contato_id)

# Rota para editar um usuário
@router.put("/contatos/update/{contato_id}")
def atualizar(contato_id: int, contato: Contato):
    return contatos_controllers.atualizar_contatos(contato_id=contato_id, nome=contato.nome, numero_telefone=contato.numero_telefone)
