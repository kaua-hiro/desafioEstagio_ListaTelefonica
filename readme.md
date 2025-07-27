# API de Lista Telefônica com FastAPI

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

## Sobre o Projeto

Esta é uma API RESTful para gerenciamento de contatos pessoais, construída com Python e FastAPI. O projeto foi recentemente refatorado para seguir melhores práticas de desenvolvimento, tornando-se mais eficiente e escalável através da implementação de injeção de dependências para gerenciar as sessões do banco de dados SQLite. A arquitetura atual oferece uma base sólida e flexível para futuras expansões e melhorias.

## Funcionalidades Atuais

- **CRUD completo de Contatos:** Operações de Criar, Ler, Atualizar e Deletar contatos de forma completa e intuitiva.
- **Gestão de Conexão Eficiente:** Utilização do sistema de dependências do FastAPI para gerenciar o ciclo de vida da conexão com o banco de dados de forma otimizada.
- **Validação de Dados:** Implementação do Pydantic para validar rigorosamente os dados de entrada nas requisições, garantindo integridade e consistência.
- **Documentação Automática:** Geração automática de documentação interativa e abrangente através do Swagger UI e ReDoc.

## Próximos Passos (Roadmap)

- [ ] **Autenticação de Usuários:** Implementar sistema completo de registro e login com tokens JWT para que cada usuário gerencie apenas seus próprios contatos de forma segura.
- [ ] **Paginação:** Adicionar sistema de paginação nas rotas de listagem para lidar eficientemente com grandes volumes de dados.
- [ ] **Busca e Filtros:** Implementar funcionalidades avançadas de busca por contatos através de nome ou parte do número telefônico.
- [ ] **Frontend:** Desenvolver uma interface de usuário moderna e responsiva com um framework atual (React, Vue) para consumir a API.
- [ ] **Containerização:** Criar um `Dockerfile` completo para facilitar o processo de deploy e garantir um ambiente de execução consistente.
- [ ] **Testes Automatizados:** Implementar uma suíte completa de testes unitários e de integração utilizando `pytest`.

## Tecnologias Utilizadas

- **Python 3** - Linguagem de programação principal
- **FastAPI** - Framework web moderno e de alta performance
- **Pydantic** - Biblioteca para validação de dados e serialização
- **SQLite** - Banco de dados relacional leve e eficiente
- **Uvicorn** - Servidor ASGI para execução da aplicação

## Estrutura do Projeto

```
/
├── database/
│   └── db.py
├── models/
│   └── user_model.py
├── controllers/
│   └── contatos_controllers.py
├── routes/
│   └── rotas.py
├── .gitignore
├── banco.db
├── main.py
└── requirements.txt
```

## Como Executar o Projeto

### Pré-requisitos
- Python 3.7 ou superior instalado em sua máquina

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/kaua-hiro/lista_telefonica_fastapi
   cd lista_telefonica_fastapi
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   # No Linux/Mac
   python -m venv venv
   source venv/bin/activate
   
   # No Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação da API**
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## Endpoints da API

| Método HTTP | Endpoint | Descrição | Necessita de Autenticação |
|-------------|----------|-----------|---------------------------|
| GET | `/contatos` | Lista todos os contatos cadastrados | Não (ainda) |
| GET | `/contatos/{contato_id}` | Busca um contato específico por ID | Não (ainda) |
| POST | `/contatos` | Cria um novo contato | Não (ainda) |
| PUT | `/contatos/update/{contato_id}` | Atualiza as informações de um contato existente | Não (ainda) |
| DELETE | `/contatos/delete/{contato_id}` | Remove um contato do sistema | Não (ainda) |

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
