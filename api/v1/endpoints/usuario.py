from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.future import select
from core.deps import get_session

from sqlalchemy.ext.asyncio import AsyncSession
from schemas.usuario_schema import UsuariosSchemaBase
from models.usuario_model import UsuarioModel

router = APIRouter()

@router.get('/', response_model=List[UsuariosSchemaBase])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuariosSchemaBase] = result.scalars().unique().all()
        return usuarios
