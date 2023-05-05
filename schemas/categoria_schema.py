from ast import List
from typing import Optional
from pydantic import BaseModel

from schemas.produto_schema import ProdutoSchema

class CategoriaSchema(BaseModel):
   id: Optional[int] = None
   descricao: str
   icone: str
   ativa: bool = True

   class Config:
      orm_mode: True

class CategoriaSchemaProdutos(CategoriaSchema):
   produtos: Optional[List[ProdutoSchema]]
