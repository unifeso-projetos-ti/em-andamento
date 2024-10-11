from pydantic import BaseModel
from typing import Optional


class EventoSchema(BaseModel):
    titulo: str
    descricao: str
    duracao: str
    classificacao: str
    horario: str
    data: str
    sala: str
    num_lugares: int

class EventoSchemaUpdate(EventoSchema):
    titulo: Optional[str]
    descricao: Optional[str]
    duracao: Optional[str]
    classificacao: Optional[str]
    horario: Optional[str]
    data: Optional[str]
    sala: Optional[str]
    num_lugares: Optional[str]