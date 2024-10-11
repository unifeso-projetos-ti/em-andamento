from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Evento(Base):
    __tablename__ = "evento"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String)
    descricao = Column(String)
    duracao = Column(String)
    classificacao = Column(String)
    horario = Column(String)
    data = Column(String)
    sala = Column(String)
    num_lugares = Column(Integer)

    # Relacionamento com Ingresso
    ingressos = relationship("Ingresso", back_populates="evento")
