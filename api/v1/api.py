from fastapi import APIRouter
<<<<<<< HEAD

from api.v1.endpoints import usuario, categoria

api_router = APIRouter()
api_router.include_router(usuario.router, prefix='/usuarios', tags=['Usuarios'])
api_router.include_router(categoria.router, prefix='/categoria', tags=['Categoria'])
=======
from api.v1.endpoints import (usuario,categoria)

api_router = APIRouter()
api_router.include_router(
    usuario.router, prefix='/usuarios', tags=['Usuarios']
)
>>>>>>> 832ce3b2250a9447fa443bbb9906a723e922956f

api_router.include_router(
   categoria.router, prefix='/categorias', tags=['Categorias']
)