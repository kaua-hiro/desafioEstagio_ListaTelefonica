# utils/security.py

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext

# --- Configurações de Segurança ---

# IMPORTANTE: Mude esta chave para uma string aleatória e segura!
# Você pode gerar uma no terminal com: openssl rand -hex 32
SECRET_KEY = "sua-chave-secreta-muito-dificil-de-adivinhar"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # O token expira em 30 minutos

# Cria um contexto para o hashing, especificando o algoritmo bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Funções ---

def verificar_senha(senha_plana: str, senha_hasheada: str) -> bool:
    """Verifica se a senha fornecida corresponde ao hash armazenado."""
    return pwd_context.verify(senha_plana, senha_hasheada)

def gerar_hash_senha(senha: str) -> str:
    """Gera o hash de uma senha usando bcrypt."""
    return pwd_context.hash(senha)

def criar_token_acesso(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Cria um novo token de acesso JWT."""
    dados_para_codificar = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Define um tempo de expiração padrão se não for fornecido
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados_para_codificar.update({"exp": expire})

    # Codifica os dados no token JWT
    token_jwt_codificado = jwt.encode(dados_para_codificar, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt_codificado