from fastapi import FastAPI
from database import Base, engine
from evento.controller import evento_router
from ingresso.controller import ingresso_router
from usuario.controller import usuario_router

app = FastAPI(
    version="0.0.1",
    title="IngressosAPI - UNIFESO",
    description="API para o gerenciamento de ingressos",
    contact={
        "name": "Grupo 1",
        "email": "gabriel.medina.fis@gmail.com"
    }
)

app.include_router(evento_router)
app.include_router(ingresso_router)
app.include_router(usuario_router)

Base.metadata.create_all(bind=engine)
