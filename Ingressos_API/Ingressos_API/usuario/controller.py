from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from usuario.model import Usuario
from usuario.schema import UsuarioSchemaBase, UsuarioSchemaRetrieve, UsuarioSchemaUpdate, UsuarioSchemaCreate
from auth import autentificar, criar_token_acesso, generate_hash, get_current_user
from database import SessionLocal


usuario_router = APIRouter(prefix="/usuario")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# GET Logado
@usuario_router.get('/logado',
                     response_model=UsuarioSchemaBase,
                     summary='Buscar o usuário logado',
                     description='Esta rota é responsavel por buscar o usuário logado no momento',
                     tags=['Usuario'])
def get_logado(usuario_logado: Usuario = Depends(get_current_user)):
    return usuario_logado


# POST Singup
@usuario_router.post('/singup',
                     response_model=UsuarioSchemaBase,
                     summary='Registrar Usuário',
                     description='Esta rota é responsavel por criar/cadastrar um usuário',
                     status_code=status.HTTP_201_CREATED,
                     tags=['Usuario'])
def post_usuario(usuario: UsuarioSchemaCreate, db: Session = Depends(get_db)):
    novo_usuario: Usuario = Usuario(nome=usuario.nome, sobrenome=usuario.sobrenome,
                                              email=usuario.email, admin=usuario.admin, senha=generate_hash(usuario.senha))
    try:
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        
        return novo_usuario
        
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Já existe um usuario com esse email cadastrado!')


# POST Login
@usuario_router.post('/login',
                     summary='Login de um Usuário',
                     description='Esta rota é responsavel pelo acesso/login do usuário',
                     tags=['Usuario'])
def post_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = autentificar(email=form_data.username, senha=form_data.password, db=db)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Dados de acesso incorretos')
        
    return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)


# GET Usuarios
@usuario_router.get('/',
                     response_model=List[UsuarioSchemaBase],
                     summary='Listar Usuários',
                     description='Esta rota é responsavel por listar os usuários da API',
                     tags=['Usuario'])
def get_usuarios(db: Session = Depends(get_db)):
    query = select(Usuario)
    result = db.execute(query)
    usuarios: List[UsuarioSchemaBase] = result.scalars().unique().all()
        
    return usuarios


# GET Usuario
@usuario_router.get('/{usuario_id}',
                     response_model=UsuarioSchemaRetrieve,
                     summary='Obter dados do usuário',
                     description='Esta rota é responsavel por obter os dados de um usuário passando o seu ID na URI',
                     status_code=status.HTTP_200_OK,
                     tags=['Usuario'])
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    query = select(Usuario).filter(Usuario.id == usuario_id)
    result = db.execute(query)
    usuario: UsuarioSchemaRetrieve = result.scalars().unique().one_or_none()
        
    if usuario:
        return usuario
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado')


#PUT Usuario
@usuario_router.put('/{usuario_id}',
                     response_model=UsuarioSchemaUpdate,
                     summary='Alterar dados do usuário',
                     description='Esta rota é responsavel por alterar os dados de um usuário passando o seu ID na URI',
                     status_code=status.HTTP_202_ACCEPTED,
                     tags=['Usuario'])
def put_usuario(usuario_id: int, usuario: UsuarioSchemaUpdate, db: Session = Depends(get_db)):
    query = select(Usuario).filter(Usuario.id == usuario_id)
    result = db.execute(query)
    usuario_up: Usuario = result.scalars().unique().one_or_none()

    if not usuario_up:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado')

    try:
        if usuario.nome is not None:
            usuario_up.nome = usuario.nome
        if usuario.sobrenome is not None:
            usuario_up.sobrenome = usuario.sobrenome
        if usuario.email is not None:
            usuario_up.email = usuario.email
        if usuario.admin is not None:
            usuario_up.admin = usuario.admin
        if usuario.senha is not None:
            usuario_up.senha = generate_hash(usuario.senha)

        db.commit()
        db.refresh(usuario_up)
        return usuario_up
    
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail='Erro ao atualizar o usuário')


# DELETE Usuario
@usuario_router.delete('/{usuario_id}',
                        summary='Deletar um usuário',
                        description='Esta rota é responsavel por deletar um usuário passando o seu ID na URI',
                        status_code=status.HTTP_204_NO_CONTENT,
                        tags=['Usuario'])
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    query = select(Usuario).filter(Usuario.id == usuario_id)
    result = db.execute(query)
    usuario_down: UsuarioSchemaBase = result.scalars().unique().one_or_none()
        
    if not usuario_down:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado')
    
    try:
        db.delete(usuario_down)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail='Erro ao deletar o usuário')
