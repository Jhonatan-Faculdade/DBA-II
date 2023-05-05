<<<<<<< HEAD
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
=======
from typing import Optional
from pydantic import BaseModel


class CategoriaSchema(BaseModel):
    id: Optional[int] = None
    descricao: str
    icone: Optional[str]
    ativa: bool = True
    
    class Config:
        orm_mode: True
>>>>>>> 832ce3b2250a9447fa443bbb9906a723e922956f
