from pydantic import BaseModel
from typing import Optional


class IngressoSchema(BaseModel):
    id: Optional[int] = None
    num_pedido: str
    evento_id: Optional[int] = None
    usuario_id: Optional[int] = None