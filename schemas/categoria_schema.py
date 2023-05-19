from ast import List
from typing import Optional
from pydantic import BaseModel

<<<<<<< HEAD
from schemas.produtos_schema import ProdutoSchema
=======
from schemas.produto_schema import ProdutoSchema
>>>>>>> ccc132a80a70250c0b6e32c20b03c863ff38c16a

class CategoriaSchema(BaseModel):
   id: Optional[int] = None
   descricao: str
   icone: str
   ativa: bool = True

   class Config:
      orm_mode: True

class CategoriaSchemaProdutos(CategoriaSchema):
<<<<<<< HEAD
   produtos: Optional[List[ProdutoSchema]]
=======
   produtos: Optional[List[ProdutoSchema]]
>>>>>>> ccc132a80a70250c0b6e32c20b03c863ff38c16a
