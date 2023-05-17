from typing import Optional
from pydantic import BaseModel, HttpUrl
from sqlalchemy import Date

class ProdutoFotosSchema(BaseModel):
   id = Optional[int] = None
   produto_id = Optional[int]
   url = HttpUrl
   descricao = str
   data = Date
   
   class Config:
      orm_mode = True