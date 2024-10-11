from fastapi import APIRouter, Depends
from fastapi import status
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ingresso.repository import get_db, listar_ingressos_comprados, buscar_ingresso_por_id, comprar_ingresso, \
    devolver_ingresso_por_id, devolver_ingresso_por_num_pedido, alterar_ingresso
from auth import get_current_user
from usuario.model import Usuario
from ingresso.schema import IngressoSchema
    

ingresso_router = APIRouter(prefix="/ingresso")


@ingresso_router.get('/',
                     summary='Listar Todos os Ingressos',
                     description='Esta rota é responsavel por listar todos os ingressos',
                     tags=['Ingresso'])
def get_todos_ingressos_comprados(db: Session = Depends(get_db), usuario_logado: Usuario = Depends(get_current_user)):
    response = listar_ingressos_comprados(db, usuario_logado)

    return response


@ingresso_router.get('/{id_ingresso}',
                     summary='Buscar Ingresso Por Id',
                     description='Esta rota é responsavel por listar ingressos com base em seus IDs',
                     tags=['Ingresso'],
                     status_code=status.HTTP_200_OK)
def get_ingresso_por_id(id_ingresso: int, db: Session = Depends(get_db), usuario_logado: Usuario = Depends(get_current_user)):
    response = buscar_ingresso_por_id(db, id_ingresso, usuario_logado)

    if response:
       return response
   
    else:
        raise HTTPException(detail='Ingresso não encontrado', status_code=status.HTTP_404_NOT_FOUND)


@ingresso_router.post('/',
                      summary='Comprar Ingresso',
                      description='Esta rota é responsavel por comprar ingressos, sendo necessário o envio do ID do '
                                  'evento desejado. É necessário a autenticação do usuário para compra',
                      tags=['Ingresso'],
                      status_code=status.HTTP_201_CREATED)
def post_ingresso(id_evento: int, db: Session = Depends(get_db), usuario_logado: Usuario = Depends(get_current_user)):
    
    response = comprar_ingresso(db, id_evento, usuario_logado)

    if response:
        return response
    
    else:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Não foi possível completar a compra.")
   

@ingresso_router.delete('/{id}',
                        summary='Devolver Ingresso Usando Id',
                        description='Esta rota é responsavel pela devolução de ingressos com base no ID.'
                                    'É necessário a autenticação do usuário para deleção',
                        tags=['Ingresso'],
                        status_code=status.HTTP_204_NO_CONTENT)
def delete_ingresso_por_id(id_evento: int, db: Session = Depends(get_db),
                           usuario_logado: Usuario = Depends(get_current_user)):
    response = devolver_ingresso_por_id(db, id_evento, usuario_logado)

    if response:
        return response
    
    else:
        raise HTTPException(detail='Evento não encontrado', status_code=status.HTTP_404_NOT_FOUND)


@ingresso_router.delete('/',
                        summary='Devolver Ingresso Usando Numero de pedido',
                        description='Esta rota é responsavel pela devolução de ingressos com base no numero do pedido'
                                    'É necessário a autenticação do usuário para deleção',
                        tags=['Ingresso'],
                        status_code=status.HTTP_204_NO_CONTENT)
def delete_ingresso_por_num_pedido(nume_pedido: str, db: Session = Depends(get_db),
                                   usuario_logado: Usuario = Depends(get_current_user)):
    response = devolver_ingresso_por_num_pedido(db, nume_pedido, usuario_logado)

    if response:
        return response
    
    else:
        raise HTTPException(detail='Ingresso não encontrado', status_code=status.HTTP_404_NOT_FOUND)


@ingresso_router.put('/{id}',
                        summary='Alterar Ingresso Usando Id',
                        description='Esta rota é responsavel pela alteração de ingressos com base no ID'
                                    'É necessário a autenticação do usuário para alteração',
                        tags=['Ingresso'],
                        status_code=status.HTTP_200_OK)
def put_ingresso(id_evento: int, ingresso: IngressoSchema, db: Session = Depends(get_db),
                 usuario_logado: Usuario = Depends(get_current_user)):
    response = alterar_ingresso(db, id_evento, ingresso, usuario_logado)

    if response:
       return response
   
    else:
        raise HTTPException(detail='Ingresso não encontrado', status_code=status.HTTP_404_NOT_FOUND)
