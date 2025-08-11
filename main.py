# main.py

from fastapi import FastAPI
from routes import rotas
from routes import auth_routes
from models import contato_model
from models import user_model

contato_model.criar_tabela()
user_model.criar_tabela_usuarios()

app = FastAPI(
    title="API de Lista Telefônica",
    description="Um projeto de API para gerenciar uma lista de contatos.",
    version="1.2"
)

app.include_router(auth_routes.router)
app.include_router(rotas.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Lista Telefônica!"}