# 📞 API de Lista Telefônica com FastAPI

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**Uma API RESTful moderna e segura para gerenciamento de contatos pessoais**

[Demo](#-como-executar) · [Documentação](#-endpoints-da-api) · [Contribuir](#-contribuindo) · [Licença](#-licença)

</div>

---

## 🎯 Sobre o Projeto

Esta é uma **API RESTful completa** para gerenciamento de contatos pessoais, construída com **Python** e **FastAPI**. A aplicação permite que múltiplos usuários se registrem e gerenciem suas próprias listas de contatos de forma **privada e segura**, utilizando autenticação baseada em **tokens JWT**.

### 🏗️ Arquitetura
O projeto segue as **melhores práticas de desenvolvimento**:
- ✅ Arquitetura em camadas (routes, controllers, models)
- ✅ Injeção de dependências para gerenciamento do banco de dados
- ✅ Separação clara de responsabilidades
- ✅ Código limpo e bem estruturado

## ⭐ Funcionalidades

### 🔐 Autenticação e Segurança
- **Sistema de registro e login** seguro com hashing de senhas
- **Autenticação JWT** para proteção de rotas
- **Autorização baseada em usuário** - cada usuário só acessa seus próprios contatos

### 📋 Gerenciamento de Contatos
- **CRUD completo** - Criar, Ler, Atualizar e Deletar contatos
- **Associação por usuário** - contatos vinculados ao usuário logado
- **Validação robusta** com Pydantic schemas

### 🚀 Experiência do Desenvolvedor
- **Documentação automática** com Swagger UI e ReDoc
- **Injeção de dependências** nativa do FastAPI
- **Tipagem estática** com Python type hints
- **Hot reload** para desenvolvimento ágil

## 📈 Roadmap

### 🎯 Próximas Funcionalidades

#### Tier 1: Performance e UX
- [ ] **Paginação** - Implementar `skip`/`limit` para grandes volumes de dados
- [ ] **Busca e filtros** - Busca textual por nome e filtros avançados
- [ ] **Ordenação** - Ordenar contatos por nome, data de criação, etc.
- [ ] **Validação avançada** - Formato de e-mail, telefone e força de senha

#### Tier 2: Qualidade e Robustez
- [ ] **Testes automatizados** - Suíte completa com `pytest`
- [ ] **Logging estruturado** - Logs detalhados para monitoramento
- [ ] **Rate limiting** - Proteção contra abuse da API
- [ ] **Versionamento da API** - Suporte a múltiplas versões

#### Tier 3: DevOps e Produção
- [ ] **Containerização** - Docker e Docker Compose
- [ ] **CI/CD** - GitHub Actions para testes e deploy
- [ ] **Deploy em nuvem** - Render, Heroku ou AWS
- [ ] **Monitoramento** - Health checks e métricas

## 🛠️ Stack Tecnológica

| Tecnologia | Uso | Versão |
|------------|-----|--------|
| **Python** | Linguagem principal | 3.8+ |
| **FastAPI** | Framework web | Latest |
| **Pydantic** | Validação de dados | Latest |
| **SQLite** | Banco de dados | Built-in |
| **Passlib** | Hashing de senhas | Latest |
| **python-jose** | JWT tokens | Latest |
| **Uvicorn** | ASGI server | Latest |

## 📂 Estrutura do Projeto

```
📦 lista-telefonica-api/
├── 📁 database/
│   └── 📄 db.py                    # Gestão da conexão com BD
├── 📁 models/
│   ├── 📄 contato_model.py         # Modelo de dados - Contatos
│   └── 📄 user_model.py            # Modelo de dados - Usuários
├── 📁 controllers/
│   └── 📄 contatos_controllers.py  # Lógica de negócio
├── 📁 routes/
│   ├── 📄 rotas.py                 # Endpoints dos contatos
│   └── 📄 auth_routes.py           # Endpoints de autenticação
├── 📁 schemas/
│   └── 📄 user_schema.py           # Schemas de validação
├── 📁 utils/
│   └── 📄 security.py              # Funções de segurança
├── 📄 main.py                      # Entry point da aplicação
├── 📄 requirements.txt             # Dependências Python
├── 📄 banco.db                     # Banco SQLite
└── 📄 .gitignore                   # Arquivos ignorados
```

## 🚀 Instalação e Execução

### 📋 Pré-requisitos
- **Python 3.8+** instalado
- **pip** para gerenciamento de pacotes

### ⚡ Início Rápido

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/kaua-hiro/lista_telefonica_fastapi.git
cd lista_telefonica_fastapi

# 2️⃣ Crie um ambiente virtual
python -m venv venv

# 3️⃣ Ative o ambiente virtual
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 4️⃣ Instale as dependências
pip install -r requirements.txt

# 5️⃣ Execute a aplicação
uvicorn main:app --reload
```

### 🌐 Acesso à API
Após executar, acesse:
- **API Base:** http://127.0.0.1:8000
- **Documentação Swagger:** http://127.0.0.1:8000/docs
- **Documentação ReDoc:** http://127.0.0.1:8000/redoc

## 📚 Documentação da API

### 🔐 Endpoints de Autenticação

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| `POST` | `/register` | Registra um novo usuário | ❌ |
| `POST` | `/login` | Autentica e retorna token JWT | ❌ |

**Exemplo - Registro:**
```json
POST /register
{
  "username": "usuario123",
  "email": "usuario@email.com",
  "password": "senhaSegura123"
}
```

### 📱 Endpoints de Contatos

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| `GET` | `/contatos` | Lista contatos do usuário | ✅ |
| `GET` | `/contatos/{id}` | Busca contato específico | ✅ |
| `POST` | `/contatos` | Cria novo contato | ✅ |
| `PUT` | `/contatos/update/{id}` | Atualiza contato existente | ✅ |
| `DELETE` | `/contatos/delete/{id}` | Remove contato | ✅ |

**Exemplo - Criar contato:**
```json
POST /contatos
Authorization: Bearer {seu_jwt_token}
{
  "nome": "João Silva",
  "telefone": "(11) 99999-9999",
  "email": "joao@email.com"
}
```

## 🧪 Testes

> ⚠️ **Em desenvolvimento** - Suíte de testes será implementada na próxima versão

```bash
# Futuramente...
pytest tests/
```

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Siga os passos:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### 📝 Diretrizes
- Siga o padrão de código existente
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Use commits semânticos

## 📊 Estatísticas do Projeto

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/kaua-hiro/lista_telefonica_fastapi)
![GitHub contributors](https://img.shields.io/github/contributors/kaua-hiro/lista_telefonica_fastapi)
![GitHub stars](https://img.shields.io/github/stars/kaua-hiro/lista_telefonica_fastapi?style=social)
![GitHub forks](https://img.shields.io/github/forks/kaua-hiro/lista_telefonica_fastapi?style=social)

</div>

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

**[⬆ Voltar ao topo](#-api-de-lista-telefônica-com-fastapi)**

Desenvolvido com ❤️ por [Kauã Hiro](https://github.com/kaua-hiro)

⭐ Se este projeto te ajudou, considere dar uma estrela!

</div>
