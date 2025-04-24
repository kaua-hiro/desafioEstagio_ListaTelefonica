# from fastapi import Request, Form
# from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates
# from models import user_model

# # Importando o modelo de usuário
# templates = Jinja2Templates(directory="templates")

# user_model.criar_tabela()

# #MOSTRA contato
# def mostrar_contatos()-> list[dict]:
#     return user_model.listar_contatos()

# #BUSCA contatoS
# def buscar_contatos_por_id(contato_id: int) -> dict:
#     contato = user_model.buscar_contatos_por_id(contato_id)
#     return contato

# #CRIAR contato
# async def cadastrar_contatos(nome: str, numero_telefone: str)-> dict:
#     contato_id = user_model.inserir_contato(nome, numero_telefone)
#     return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}

# #EXCLUI contato
# def excluir_contatos(contato_id: int) -> dict:
#     user_model.excluir_contatos(contato_id)
#     return {"message": "Usuário excluído com sucesso."}

# #EDITAR/ATUALIZA contato
# def atualizar_contatos(contato_id: int, nome: str, numero_telefone: str) -> dict:
#     user_model.atualizar_contatos(contato_id, nome, numero_telefone)
#     return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}

from fastapi import Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import user_model

# Importando o modelo de usuário
templates = Jinja2Templates(directory="templates")

# Criando a tabela de contatos
user_model.criar_tabela()

# MOSTRA contato
def mostrar_contatos() -> list[dict]:
    try:
        return user_model.listar_contatos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar contatos: {str(e)}")

# BUSCA contato
def buscar_contatos_por_id(contato_id: int) -> dict:
    try:
        contato = user_model.buscar_contatos_por_id(contato_id)
        if contato is None:
            raise HTTPException(status_code=404, detail="Contato não encontrado")
        return contato
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contato: {str(e)}")

# CRIAR contato
async def cadastrar_contatos(nome: str, numero_telefone: str) -> dict:
    try:
        contato_id = user_model.inserir_contato(nome, numero_telefone)
        return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar contato: {str(e)}")

# EXCLUI contato
def excluir_contatos(contato_id: int) -> dict:
    try:
        user_model.excluir_contatos(contato_id)
        return {"message": "Usuário excluído com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir contato: {str(e)}")

# EDITAR/ATUALIZA contato
def atualizar_contatos(contato_id: int, nome: str, numero_telefone: str) -> dict:
    try:
        user_model.atualizar_contatos(contato_id, nome, numero_telefone)
        return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar contato: {str(e)}")
