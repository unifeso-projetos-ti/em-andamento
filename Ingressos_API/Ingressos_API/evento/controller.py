from fastapi import APIRouter, Depends
from fastapi import status
from fastapi import HTTPException

from sqlalchemy.orm import Session

from evento.repository import get_db, listar_todos_eventos, buscar_evento_por_id, criar_evento, deletar_evento, alterar_evento
from evento.schema import EventoSchema, EventoSchemaUpdate


evento_router = APIRouter(prefix="/evento")


@evento_router.get('/',
                   summary='Listar Todos os Eventos',
                   description='Esta rota é responsavel por listar todos os eventos catalogados no banco de dados',
                   tags=['Evento'])
def get_todos_eventos(db: Session = Depends(get_db)):
    response = listar_todos_eventos(db)

    return response


@evento_router.get('/{id}',
                   summary='Buscar Por um Evento Usando Id',
                   description='Esta Rota é responsavel por buscar um evento baseado no ID passado como parametro na '
                               'URI',
                   tags=['Evento'],
                   status_code=status.HTTP_200_OK)
def get_evento_por_id(id_evento: int, db: Session = Depends(get_db)):
    response = buscar_evento_por_id(db, id_evento)

    if response:
       return response
    else:
        raise HTTPException(detail='Evento não encontrado', status_code=status.HTTP_404_NOT_FOUND)


@evento_router.post('/', summary='Criar Evento',
                    description='Esta Rota é responsavel pela crianção de novos eventos, ela tem como pré requisito '
                                'um request body com as informções do Evento',
                    tags=['Evento'],
                    status_code=status.HTTP_201_CREATED)
def post_evento(evento: EventoSchema, db: Session = Depends(get_db)):
    response = criar_evento(db, evento)

    return response


@evento_router.delete('/{id}', summary='Deletar Evento Usando Id',
                      description='Esta Rota é responsavel por Deletar um evento, ela exige um parametro ID na URI '
                                  'para localizar o item que deve ser Deletado',
                      tags=['Evento'],
                      status_code=status.HTTP_204_NO_CONTENT)
def delete_evento(id_evento: int, db: Session = Depends(get_db)):
    response = deletar_evento(db, id_evento)
    
    if response:
        return response
    
    else:
        raise HTTPException(detail='Evento não encontrado', status_code=status.HTTP_404_NOT_FOUND)
    
    
@evento_router.put('/{id}',
                   summary='Alterar um Evento Usando Id',
                   description='Esta Rota é responsavel por Alterar um evento, ela exige um parametro ID na URI'
                               'para localizar o item que deve ser Alterado',
                   tags=['Evento'],
                   status_code=status.HTTP_200_OK)
def put_evento(id_evento: int, evento: EventoSchemaUpdate, db: Session = Depends(get_db)):
    response = alterar_evento(db, id_evento, evento)

    if response:
       return response
    else:
        raise HTTPException(detail='Evento não encontrado', status_code=status.HTTP_404_NOT_FOUND)


        

