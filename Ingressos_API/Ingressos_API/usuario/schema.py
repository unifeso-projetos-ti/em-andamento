from typing import List, Optional

from pydantic import BaseModel, EmailStr

from ingresso.schema import IngressoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    admin: bool = False
    
    class Config:
        from_attributes = True

        
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
  
    
class UsuarioSchemaRetrieve(UsuarioSchemaBase):
    ingressos: Optional[List[IngressoSchema]]
    

class UsuarioSchemaUpdate(UsuarioSchemaBase):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    admin: Optional[bool] = None
    