# routes/auth_routes.py

import sqlite3
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt

from models import user_model
from schemas import user_schema
from utils import security
from database.db import get_db

router = APIRouter(tags=["Autenticação"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/register", response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(usuario: user_schema.UserCreate, db: sqlite3.Connection = Depends(get_db)):
    db_user = user_model.buscar_usuario_por_email(db, email=usuario.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    novo_usuario = user_model.criar_usuario(db=db, usuario=usuario)
    return novo_usuario

@router.post("/login", response_model=user_schema.Token)
def login_for_access_token(db: sqlite3.Connection = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_model.buscar_usuario_por_email(db, email=form_data.username)
    if not user or not security.verificar_senha(form_data.password, user["senha_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.criar_token_acesso(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_active_user(token: str = Depends(oauth2_scheme), db: sqlite3.Connection = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = user_model.buscar_usuario_por_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user