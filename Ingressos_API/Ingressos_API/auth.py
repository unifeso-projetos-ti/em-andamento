from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic_settings import BaseSettings

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from passlib.context import CryptContext
import bcrypt

from sqlalchemy.orm import Session
from sqlalchemy.future import select

from pytz import timezone
from datetime import datetime, timedelta

from database import SessionLocal
from usuario.model import Usuario


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Settings(BaseSettings):
    JWT_SECRET: str = 'hSZXWXIU3KAV_1IzTf_Vg5tZzEfJl2Jm3Qo1RCpaZ4g'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    class Config:
        case_sensitive = True

settings = Settings()


CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

        
def verify_password(senha: str, hash_senha: str) -> bool:
    
    return CRIPTO.verify(senha, hash_senha)


def generate_hash(senha: str):
    
    return CRIPTO.hash(senha)


class TokenData(BaseModel):
    username: Optional[str] = None
    
    
oath2_schema = OAuth2PasswordBearer(
    tokenUrl=f"/usuario/login")

    
def autentificar(email: EmailStr, senha: str, db: Session) -> Optional[Usuario]:
    query = select(Usuario).filter(Usuario.email == email)
    result = db.execute(query)
    usuario: Usuario = result.scalars().unique().one_or_none()
        
    if not usuario:
        return None
        
    if not verify_password(senha, usuario.senha):
        return None
        
    return usuario

    
def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    payload = {}
    sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=sp) + tempo_vida
    
    payload["type"] = tipo_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)
    
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
    

def criar_token_acesso(sub: str) -> str:
    
    return _criar_token(
        tipo_token = 'access_token',
        tempo_vida = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub = sub
    )
    
def get_current_user(db: Session = Depends(get_db),
                           token: str = Depends(oath2_schema,)
                           )-> Usuario:
    credential_exception: HTTPException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                                        detail='Não foi possível autentificar a credencial',
                                                        headers={"WWW-Authenticate": "Bearer"}
                                                        )
    
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False}
        )
        username: str = payload.get("sub")
        
        if username is None:
            raise credential_exception
        
        token_data = TokenData(username = username)
    except JWTError:
        raise credential_exception
    
    query = select(Usuario).filter(Usuario.id == int(token_data.username))
    result = db.execute(query)
    usuario: Usuario = result.scalars().unique().one_or_none()
        
    if usuario is None:
        raise credential_exception
        
    return usuario
