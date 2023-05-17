from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Date

class RestauranteSchema(BaseModel):
   id = Optional[int] = None
   nome = str
   endereco = str
   telefone = str
   valorMinimo = float
   horariosFuncionamento = Date
   formaEntrega = str
   formaPagamento = str
   categorias = str

   class Config:
      orm_mode = True