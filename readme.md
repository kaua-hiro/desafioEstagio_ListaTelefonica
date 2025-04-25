# Aula 1 FastAPI
Instalando o Fastapi 
```
pip install "fastapi[standard]"
```
Criando um servidor fastapi simples Crie um arquivo main.py:
Rodando o servidor 1ª forma
```
fastapi dev main.py
```
Rodando o servidor 2ª forma
```
python main.py
```
Instalar a biblioteca:
```
pip install jinja2
```


Lista Telefônica - API MVC com FastAPI Descrição do Projeto Este projeto implementa uma API de lista telefônica com operações CRUD (Create, Read, Update, Delete) utilizando a arquitetura MVC (Model-View-Controller). Desenvolvido como um desafio de estágio, o sistema permite gerenciar contatos telefônicos e está preparado para futuras implementações como cadastro de usuários, autenticação e controle de acesso. Tecnologias Utilizadas

Python 3.6+ FastAPI SQLite Uvicorn (servidor ASGI) Pydantic (validação de dados)

Criar contato: Adiciona um novo contato à lista telefônica Listar contatos: Exibe todos os contatos cadastrados Buscar contato: Localiza um contato específico por ID Atualizar contato: Modifica informações de um contato existente Excluir contato: Remove um contato da lista

Funcionalidades Futuras

Cadastro de usuários Sistema de login e autenticação Níveis de acesso diferenciados Vinculação de listas telefônicas a usuários específicos

Como Configurar e Executar o Projeto Pré-requisitos

Python 3.6 ou superior Pip (gerenciador de pacotes Python)

Instalação

Clone o repositório: git clone https://github.com/kaua-hiro/lista-telefonica.git cd lista-telefonica

Crie um ambiente virtual (opcional, mas recomendado):

Windows
python -m venv venv venv\Scripts\activate

Linux/MacOS
python -m venv venv source venv/bin/activate

Instale as dependências: pip install -r requirements.txt Conteúdo sugerido para o arquivo requirements.txt: fastapi>=0.68.0 uvicorn>=0.15.0 pydantic>=1.8.0

Inicializando a Aplicação

Certifique-se de que está no diretório raiz do projeto. Execute o comando: uvicorn main:app --reload

O parâmetro main refere-se ao arquivo main.py O parâmetro app refere-se à instância do FastAPI definida nesse arquivo A flag --reload permite que o servidor reinicie automaticamente quando detectar alterações no código

A API estará disponível em http://localhost:8000 A documentação automática da API estará disponível em:

Swagger UI: http://localhost:8000/docs ReDoc: http://localhost:8000/redoc

Exemplo do Arquivo Principal (main.py) pythonfrom fastapi import FastAPI from rotas import router

app = FastAPI( title="API Lista Telefônica", description="API para gerenciamento de contatos telefônicos com arquitetura MVC", version="1.0.0" )

Incluindo as rotas da aplicação
app.include_router(router)

Cria as tabelas necessárias no banco de dados ao iniciar a aplicação
@app.on_event("startup") async def startup_event(): from models.user_model import criar_tabela criar_tabela()

if name == "main": import uvicorn uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) Como Usar a API Endpoints Disponíveis Criar Contato (POST)

Endpoint: /contatos Body (JSON): json{ "nome": "Nome do Contato", "numero_telefone": "123456789" }

Resposta (200 OK): json{ "id": 1, "nome": "Nome do Contato", "numero_telefone": "123456789" }

Listar Todos os Contatos (GET)

Endpoint: /contatos Resposta (200 OK): json[ { "id": 1, "nome": "Nome do Contato", "numero_telefone": "123456789" }, { "id": 2, "nome": "Outro Contato", "numero_telefone": "987654321" } ]

Buscar Contato por ID (GET)

Endpoint: /contatos/{id} Resposta (200 OK): json{ "id": 1, "nome": "Nome do Contato", "numero_telefone": "123456789" }

Resposta (404 Not Found): json{ "detail": "Contato não encontrado" }

Atualizar Contato (PUT)

Endpoint: /contatos/{id} Body (JSON): json{ "nome": "Nome Atualizado", "numero_telefone": "999999999" }

Resposta (200 OK): json{ "id": 1, "nome": "Nome Atualizado", "numero_telefone": "999999999" }

Excluir Contato (DELETE)

Endpoint: /contatos/{id} Resposta (200 OK): json{ "message": "Contato excluído com sucesso" }

Testando a API Você pode testar a API usando:

Insomnia ou Postman: Ferramentas gráficas para testar APIs Swagger UI: Disponível em http://localhost:8000/docs Curl: Via linha de comando

Exemplo de teste com curl: bash# Listar todos os contatos curl -X GET http://localhost:8000/contatos

Adicionar um contato
curl -X POST http://localhost:8000/contatos
-H "Content-Type: application/json"
-d '{"nome": "João Silva", "numero_telefone": "123456789"}' Próximos Passos para Implementações Futuras Cadastro de Usuários

Criar modelo de usuários Implementar endpoints para registro e gerenciamento de usuários

Autenticação

Implementar sistema de login simples Adicionar middleware de autenticação Criar sistema de sessões para usuários

Controle de Acesso

Definir níveis de permissão Implementar validação de permissões nos endpoints

Vinculação de Contatos a Usuários

Adicionar campo de usuário_id na tabela de contatos Filtrar contatos por usuário autenticado

Contribuição Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Licença Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
