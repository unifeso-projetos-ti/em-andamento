import random
import string

from sqlalchemy.orm import Session

from database import SessionLocal
from evento.repository import buscar_evento_por_id_retorna_evento
from ingresso.model import Ingresso
from usuario.model import Usuario


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def comprar_ingresso(db: Session, id_evento: int, usuario_logado: Usuario):
    # Busca o evento pelo ID
    evento = buscar_evento_por_id_retorna_evento(db, id_evento)

    # Verifica se o evento existe
    if not evento:
        return {'Ingresso': 'Evento não encontrado!'}
    
    # Verfica se o usuário está autenticado
    if not usuario_logado:
        return {'Usuário': 'Usuário não autenticado!'}

    # Cria o ingresso
    _ingresso = Ingresso(
        num_pedido=_gerar_numero_pedido(),
        evento_id=evento.id,
        usuario_id = usuario_logado.id
    )

    try:
        db.add(_ingresso)
        db.commit()
        db.refresh(_ingresso)
        return {'Ingresso': 'Ingresso comprado com sucesso!'}
    except Exception as e:
        db.rollback()  # Faz rollback para evitar problemas no banco de dados
        return {'Ingresso': f'Erro durante a compra do ingresso! \n {e}'}
    
    
def listar_ingressos_comprados(db: Session, usuario_logado: Usuario):
    try:
        _ingressos = db.query(Ingresso).filter(Ingresso.usuario_id == usuario_logado.id).all()
        if _ingressos:
            return {'Ingressos': _ingressos}
        else:
            return {'Ingresso': 'Nenhum ingresso encontrado para o usuário logado'}
    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a busca dos ingressos! \n {e}'}


def buscar_ingresso_por_id(db: Session, usuario_logado: Usuario, id_ingresso: int):
    try:
        _ingresso = db.query(Ingresso).filter(Ingresso.id == id_ingresso, Ingresso.usuario_id == usuario_logado.id).first()
        if _ingresso:
            return {'Ingresso': _ingresso}
        else:
            return {'Ingresso': 'Ingresso não encontrado para o usuário logado'}
    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a busca do ingresso! \n {e}'}


def devolver_ingresso_por_id(db: Session, usuario_logado: Usuario, id_ingresso: int):
    try:
        _ingresso = db.query(Ingresso).filter(Ingresso.id == id_ingresso, Ingresso.usuario_id == usuario_logado.id).first()
        if _ingresso:
            db.delete(_ingresso)
            db.commit()
            return {'Ingresso': 'Ingresso apagado com sucesso!'}
        else:
            return {'Ingresso': 'Ingresso não encontrado para o usuário logado'}
    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a exclusão do ingresso! \n {e}'}


def devolver_ingresso_por_num_pedido(db: Session, usuario_logado: Usuario, num_pedido: str):
    try:
        _ingresso = db.query(Ingresso).filter(Ingresso.num_pedido == num_pedido, Ingresso.usuario_id == usuario_logado.id).first()
        if _ingresso:
            db.delete(_ingresso)
            db.commit()
            return {'Ingresso': 'Ingresso apagado com sucesso!'}
        else:
            return {'Ingresso': 'Ingresso não encontrado para o usuário logado'}
    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a exclusão do ingresso! \n {e}'}


def alterar_ingresso(db: Session, usuario_logado: Usuario, num_pedido: str, ingresso: Ingresso):
    try:
        _ingresso = db.query(Ingresso).filter(Ingresso.num_pedido == num_pedido, Ingresso.usuario_id == usuario_logado.id).first()
        if _ingresso:
            _ingresso.num_pedido = _gerar_numero_pedido()
            _ingresso.evento_id = ingresso.evento_id
            db.commit()
            return {'Ingresso': 'Ingresso alterado com sucesso!'}
        else:
            return {'Ingresso': 'Ingresso não encontrado para o usuário logado'}
    except Exception as e:
        db.rollback()
        return {'Ingresso': f'Erro durante a alteração do ingresso! \n {e}'}


def _gerar_numero_pedido():
    _numero = ''.join(random.choices(string.digits, k=3))
    _caracteres = ''.join(random.choices(string.ascii_uppercase, k=3))
    _codigo = _numero + _caracteres

    return _codigo



