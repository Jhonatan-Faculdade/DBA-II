<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from sqlalchemy.future import select
from core.deps import get_session
from sqlalchemy.exc import IntegrityError

from sqlalchemy.ext.asyncio import AsyncSession
from schemas.categoria_schema import CategoriaSchema
from models.categoria_model import CategoriaModel

router = APIRouter()

@router.get('/', response_model=None)
async def get_categorias(db: AsyncSession = Depends(get_session)):
   async with db as session:
         query = select(CategoriaModel)
         result = await session.execute(query)
         categorias: List[CategoriaSchema] = result.scalars().unique().all()
         return categorias

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=None)
async def post_categoria(categoria: CategoriaSchema,
                  db: AsyncSession = Depends(get_session)):
   nova_categoria: CategoriaModel = CategoriaModel(descricao=categoria.descricao,
                                                   icone=categoria.icone,
                                                   ativa=categoria.ativa)
   async with db as session:
         try:
            session.add(nova_categoria)
            await session.commit()
            return nova_categoria
         except Exception as e:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                 detail='Ja existe essa categoria cadastrada, {e}')

@router.put('/{categoria_id}',
            response_model=None,
            status_code=status.HTTP_202_ACCEPTED)
async def put_categoria(categoria_id: int,
                     categoria: CategoriaSchema,
                     db: AsyncSession = Depends(get_session)):
   async with db as session:
      query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
      result = await session.execute(query)
      categoria_up: CategoriaSchema = result.scalars().unique().one_or_none()
      
      if categoria_up:
         if categoria.descricao:
               categoria_up.descricao = categoria.descricao
         if categoria.icone:
               categoria_up.icone = categoria.icone
         if categoria.ativa:
               categoria_up.ativa = categoria.ativa
         return categoria_up
      else:
         raise HTTPException(detail="Categoria não encontrada",
                              status_code=status.HTTP_404_NOT_FOUND)

@router.delete('/{categoria_id}', status_code=status.HTTP_404_NOT_FOUND)
async def delete_usuario(categoria_id: int, db: AsyncSession = Depends(get_session)):
   async with db as session:
      query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
      result = await session.execute(query)
      categoria_del: CategoriaSchema = result.scalars().one_or_none()

      if categoria_del:
         await session.delete(categoria_del)
         await session.commit()
         return Response(status_code=status.HTTP_204_NO_CONTENT)
      else:
         raise HTTPException(detail="Categoria não encontrada",
                              status_code=status.HTTP_404_NOT_FOUND)

@router.get('/{categoria_id}', response_model=None, status_code=status.HTTP_200_OK)
async def get_categoria(categoria_id: int, db: AsyncSession = Depends(get_session)):
   async with db as session:
      query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
      result = await session.execute(query)
      categoria: CategoriaSchema = result.scalars().one_or_none()

      if categoria:
         return categoria
      else:
         raise HTTPException(detail="Usuario não encontrado", status_code=status.HTTP_404_NOT_FOUND)
=======
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.future import select
from core.deps import get_session

from sqlalchemy.ext.asyncio import AsyncSession
from models.categoria_model import CategoriaModel

from schemas.categoria_schema import CategoriaSchema


router = APIRouter()


@router.get('/', response_model=List[CategoriaSchema])
async def get_categorias(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel)
        result = await session.execute(query)
        categorias: List[CategoriaModel] = result.scalars().all()

        return categorias


@router.get('/{categoria_id}', response_model=CategoriaSchema, status_code=status.HTTP_200_OK)
async def get_categoria(categoria_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(
            CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria = result.scalar_one_or_none()
        if categoria:
            return categoria
        else:
            raise HTTPException(detail="Categoria nao encontrada",
                                status_code=status.HTTP_404_NOT_FOUND)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CategoriaSchema)
async def post_categoria(categoria: CategoriaSchema, db: AsyncSession = Depends(get_session)):
    novo_categoria = CategoriaModel(descricao=categoria.descricao,
                                    icone=categoria.icone,
                                    eh_ativa=categoria.eh_ativa)
    db.add(novo_categoria)
    await db.commit()

    return novo_categoria


@router.put('/{categoria_id}', response_model=CategoriaSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_categoria(categoria_id: int, categoria: CategoriaSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(
            CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria_up = result.scalar_one_or_none()

        if categoria_up:
            categoria_up.descricao = categoria.descricao
            categoria_up.icone = categoria.icone
            categoria_up.eh_ativa = categoria.eh_ativa
            await session.commit()

            return categoria_up
        else:
            raise HTTPException(detail="Categoria nao encontrada",
                                status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{categoria_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria(categoria_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(
            CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria_del = result.scalar_one_or_none()

        if categoria_del:
            await session.delete(categoria_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
<<<<<<< HEAD
            raise HTTPException(detail="Categoria nao encontrada",
                                status_code=status.HTTP_404_NOT_FOUND)
=======
            raise HTTPException(detail="Usuario nao encontrado",
                                status_code=status.HTTP_404_NOT_FOUND)"""
>>>>>>> 832ce3b2250a9447fa443bbb9906a723e922956f
>>>>>>> ccc132a80a70250c0b6e32c20b03c863ff38c16a
