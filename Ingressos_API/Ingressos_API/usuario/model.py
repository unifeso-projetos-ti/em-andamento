from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), nullable=False, index=True, unique=True)
    senha = Column(String(256), nullable=False)
    admin = Column(Boolean, default=False, nullable=True)
    ingressos = relationship ("Ingresso", cascade="all,delete-orphan", uselist=True, back_populates="criador")