# 🚀 Sistema de Gerenciamento de Contatos 

## 🏗️ Arquitetura MVC

## 📝 Relatório Técnico

### 1. Arquitetura MVC Implementada

O sistema foi desenvolvido seguindo o padrão **Model-View-Controller (MVC)**, com as seguintes características:

**a) Camada Model (Models)**
```python
# user_model.py
def inserir_contato(nome: str, numero_telefone:str)-> int:
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lista_contatos (nome, numero_telefone) "
    "VALUES (?, ?)", (nome, numero_telefone))
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id
```
- Responsável pela interação com o banco SQLite
- Define a estrutura de dados e operações CRUD
- Implementa funções de busca e manipulação de registros
- Retorna None quando um contato não é encontrado, exigindo verificação adequada

**b) Camada Controller (Controllers)**
```python
# contatos_controllers.py
async def cadastrar_contatos(nome: str, numero_telefone: str) -> dict:
    try:
        contato_id = user_model.inserir_contato(nome, numero_telefone)
        return {"id": contato_id, "nome": nome, "numero_telefone": numero_telefone}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar contato: {str(e)}")
```
- Gerencia a lógica de negócios
- Realiza o tratamento de erros com try/except e HTTPException
- Coordena a comunicação entre Models e rotas
- Implementa diferentes status HTTP para cada tipo de resposta

**c) Camada View (Templates)**
- O sistema está configurado para suportar templates Jinja2
- As importações para suporte a templates estão presentes (`Jinja2Templates(directory="templates")`)
- Para completar esta camada, é necessário criar o diretório "templates" e adicionar os arquivos HTML/CSS

### 2. Sistema de Validação e Tratamento de Erros

Implementamos um sistema robusto de tratamento de erros:

**a) Tratamento de Exceções**
```python
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
```

**Respostas de Erro por Status Code:**
- 404: Contato não encontrado
- 500: Erros internos do servidor (problemas com banco de dados, etc.)

**b) Validação de Dados com Pydantic**
```python
class Contato(BaseModel):
    nome: str
    numero_telefone: str
```

### 3. Sistema de Rotas Modular

As rotas foram implementadas com:

**a) Organização Modular**
```python
# rotas.py
router = APIRouter()

@router.get("/contatos")
def pagina_inicial():
    return contatos_controllers.mostrar_contatos()

@router.post("/contatos", status_code=201)
async def cadastrar(contato: Contato):
    return await contatos_controllers.cadastrar_contatos(
        nome=contato.nome, 
        numero_telefone=contato.numero_telefone
    )
```

**b) Endpoints Disponíveis**

| Método | Endpoint | Descrição | Status Code Sucesso |
|--------|----------|-----------|---------------------|
| GET | `/contatos` | Lista todos os contatos | 200 |
| GET | `/contatos/{contato_id}` | Busca contato por ID | 200 |
| POST | `/contatos` | Cria novo contato | 201 |
| PUT | `/contatos/update/{contato_id}` | Atualiza contato existente | 200 |
| DELETE | `/contatos/delete/{contato_id}` | Remove contato | 200 |

### 4. Exemplos de Uso da API

**a) Listar Todos os Contatos**

Resposta:
```json
[
  {
    "id": 1,
    "nome": "João Silva",
    "numero_telefone": "123456789"
  },
  {
    "id": 2,
    "nome": "Maria Souza",
    "numero_telefone": "987654321"
  }
]
```

**b) Buscar Contato por ID**

Resposta:
```json
{
  "id": 1,
  "nome": "João Silva",
  "numero_telefone": "123456789"
}
```

**c) Criar Novo Contato**

Corpo da requisição:
```json
{
  "nome": "Pedro Oliveira", 
  "numero_telefone": "555666777"
}
```

Resposta:
```json
{
  "id": 3,
  "nome": "Pedro Oliveira",
  "numero_telefone": "555666777"
}
```

**d) Atualizar Contato**

Corpo da requisição:
```json
{
  "nome": "Pedro Silva", 
  "numero_telefone": "555666888"
}
```

Resposta:
```json
{
  "id": 3,
  "nome": "Pedro Silva",
  "numero_telefone": "555666888"
}
```

**e) Excluir Contato**

Resposta:
```json
{
  "message": "Usuário excluído com sucesso."
}
```

### 5. Desafios e Soluções

| Desafio | Solução Implementada | Código Exemplo |
|---------|----------------------|----------------|
| Tratamento de erros em consultas | Implementação de try/except em controllers | `try: contato = user_model.buscar_contatos_por_id(contato_id)` |
| Validação de dados | Uso do Pydantic para validação | `class Contato(BaseModel): nome: str` |
| Arquitetura escalável | Estruturação em camadas MVC | Separação em controllers, models e routes |
| Retorno adequado de status HTTP | Uso de status_code nos endpoints | `@router.post("/contatos", status_code=201)` |
| Tratamento de contatos inexistentes | Verificação explícita de resultados nulos | `if contato is None: raise HTTPException(status_code=404...)` |

## 🏗️ Estrutura do Projeto

```
sistema-contatos/
├── controllers/
│   └── contatos_controllers.py    # Lógica para contatos
│
├── database/
│   └── db.py                      # Configurações do banco
│
├── models/
│   └── user_model.py              # Modelo de contatos
│
├── routes/
│   └── rotas.py                   # Rotas da API
│
├── templates/                     # Templates para interface web (a ser implementado)
│
├── .gitignore                     # Arquivos ignorados pelo git
├── main.py                        # Aplicação principal
├── banco.db                       # Banco de dados SQLite
└── README.md                      # Documentação
```

---

## 🔄 Fluxo de Dados

1. **Requisição** chega à rota correspondente em `rotas.py`
2. **Controller** processa a requisição em `contatos_controllers.py`
3. **Model** interage com o banco em `user_model.py`
4. **Resposta** é retornada em formato JSON com status HTTP apropriado

### Diagrama de Sequência
```
Cliente HTTP → Rotas → Controllers → Models → Banco SQLite
                                  ↓
Cliente HTTP ← Resposta JSON ← Controllers
```

---

## ✅ Validações Implementadas

| Entidade | Campo           | Validações                | Status Error |
|----------|-----------------|---------------------------|--------------|
| Contato  | nome            | Obrigatório               | 422 Unprocessable Entity |
|          | numero_telefone | Obrigatório               | 422 Unprocessable Entity |

Obs: As validações são aplicadas automaticamente pelo Pydantic e FastAPI.

---

## 📊 Banco de Dados

O sistema utiliza SQLite como banco de dados, com a seguinte estrutura:

```sql
CREATE TABLE IF NOT EXISTS lista_contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    numero_telefone TEXT NOT NULL
)
```

Principais operações no banco:
- `conectar()`: Estabelece conexão com o banco SQLite
- `cursor.execute()`: Executa consultas SQL
- `cursor.fetchall()`: Recupera múltiplos registros
- `cursor.fetchone()`: Recupera um único registro
- `cursor.lastrowid`: Obtém o ID do último registro inserido
- `cursor.rowcount`: Verifica se operações de modificação foram bem-sucedidas

---

## 🚀 Como Executar

1. **Pré-requisitos**:
   - Python 3.7+
   - pip (gerenciador de pacotes do Python)

2. **Configuração**:
   ```bash
   # Clonar repositório
   git clone [https://github.com/kaua-hiro/lista_telefonica_fastapi]
   cd sistema-contatos
   
   # Criar ambiente virtual
   python -m venv venv
   
   # Ativar ambiente virtual
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   
   # Instalar dependências
   pip install fastapi uvicorn pydantic
   ```

3. **Execução**:
   ```bash
   python main.py
   ```
   Ou utilize o Uvicorn diretamente:
   ```bash
   uvicorn main:app --reload
   ```

4. **Acessando o Sistema**:
   - API: `http://127.0.0.1:8000`
   - Documentação interativa (gerada automaticamente pelo FastAPI): `http://127.0.0.1:8000/docs`
   - Interface alternativa de documentação: `http://127.0.0.1:8000/redoc`

---

## 🧪 Testando a API

Para testar a API, você pode usar:

1. **Swagger UI**: Acesse `http://127.0.0.1:8000/docs` para uma interface interativa onde pode executar todas as operações da API.

2. **Postman/Insomnia**: Importe os endpoints para testes mais elaborados.

3. **Scripts Python**: Teste programaticamente com bibliotecas como `requests`:
   ```python
   import requests
   
   # Listar contatos
   response = requests.get('http://127.0.0.1:8000/contatos')
   print(response.json())
   
   # Criar novo contato
   data = {"nome": "Teste Automatizado", "numero_telefone": "999888777"}
   response = requests.post('http://127.0.0.1:8000/contatos', json=data)
   print(response.json())
   ```
## 📊 Diagrama de Classes

O sistema segue uma arquitetura bem definida, representada pelo seguinte diagrama de classes:

![diagramaClasse_BRVANT](https://github.com/user-attachments/assets/ab2f0967-4cc8-47c1-a7ba-46584052a90f)

### Descrição das Classes

**1. Database**
- Responsável pela conexão com o banco de dados
- Fornece a engine e a sessão para acesso ao banco
- Método `get_db()` retorna uma sessão ativa

**2. CriacaoContato**
- Modelo para criação de novos contatos
- Contém apenas os campos necessários para criação (nome e telefone)
- Utilizado como entrada nas operações de criação e atualização

**3. Contato**
- Modelo principal que representa um contato no banco de dados
- Possui ID como chave primária, além de nome e telefone
- É manipulado pelo ControlleContato

**4. ContatoResponse**
- DTO (Data Transfer Object) usado para retornar informações de contatos
- Contém id, nome e telefone formatados para apresentação ao cliente
- Retornado pelas operações de CRUD

**5. ControlleContato**
- Implementa a lógica de negócios para gerenciamento de contatos
- Utiliza a sessão do banco de dados para operações de persistência
- Oferece métodos para criar, buscar, atualizar e deletar contatos
- Retorna objetos do tipo ContatoResponse

**6. RotasContato**
- Define os endpoints da API REST
- Utiliza o ControlleContato para processar as requisições
- Mapeia operações HTTP para os métodos do controller
- Gerencia os códigos de status HTTP e formatação das respostas

### Relações Principais

- `RotasContato` usa `ControlleContato` para processar as requisições
- `ControlleContato` usa `Database` para obter sessões do banco de dados
- `ControlleContato` manipula objetos `Contato` no banco de dados
- `ControlleContato` usa `CriacaoContato` como entrada para operações de criação/atualização
- `ControlleContato` retorna objetos `ContatoResponse` como resultado das operações

Esta arquitetura segue os princípios de separação de responsabilidades e permite uma manutenção mais fácil e escalabilidade do sistema.
---

## 📚 Referências Técnicas

1. **FastAPI**
   - [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)

2. **SQLite**
   - [Documentação SQLite](https://www.sqlite.org/docs.html)

3. **Pydantic**
   - [Documentação Pydantic](https://pydantic-docs.helpmanual.io/)

4. **REST API Design**
   - [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)

5. **Padrão MVC**
   - [Padrões de Arquitetura de Aplicações Corporativas](https://www.martinfowler.com/books/eaa.html)

---

<div align="center">
  Desenvolvido com Python 🐍 e FastAPI ⚡ 
</div>
