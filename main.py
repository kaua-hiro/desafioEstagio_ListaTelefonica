from fastapi import FastAPI
from routes import rotas
from models import user_model

user_model.criar_tabela()

app = FastAPI(
    title="API de Lista Telefônica",
    description="Um projeto de API para gerenciar uma lista de contatos.",
    version="1.0"
)

app.include_router(rotas.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Lista Telefônica!"}