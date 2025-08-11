from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "sua-chave-secreta-muito-dificil-de-adivinhar"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Funções ---

def verificar_senha(senha_plana: str, senha_hasheada: str) -> bool:
    return pwd_context.verify(senha_plana, senha_hasheada)

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def criar_token_acesso(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    dados_para_codificar = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados_para_codificar.update({"exp": expire})

    token_jwt_codificado = jwt.encode(dados_para_codificar, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt_codificado