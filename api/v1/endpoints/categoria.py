from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models.categoria_model import CategoriaModel
from schemas.categoria_schema import CategoriaSchema
from sqlalchemy.future import select
from core.deps import get_session


router = APIRouter()

@router.get('/', response_model=List[CategoriaSchema])
async def get_categorias(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel)
        result = await session.execute(query)
        categorias: List[CategoriaSchema] = result.scalars().unique().all()
        return categorias

@router.get('/{categoria_id}', 
            response_model=CategoriaSchema,
            status_code=status.HTTP_200_OK)
async def get_categoria(categoria_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CategoriaModel).filter(CategoriaModel.id == categoria_id)
        result = await session.execute(query)
        categoria: CategoriaSchema = result.scalars().one_or_none()
        
        if categoria:
            return categoria
        else:
            raise HTTPException(detail="Categoria nao encontrada",
                                status_code=status.HTTP_404_NOT_FOUND)

@router.post('/singup', status_code=status.HTTP_201_CREATED)
async def post_categoria(categoria: CategoriaSchema,
                       db: AsyncSession = Depends(get_session)):
    novo_categoria: CategoriaModel(
        descricao=categoria.descricao,
        icone=categoria.icone,
        ativa=categoria.ativa)
    
    async with db as session:
        try:
            session.add(novo_categoria)
            await session.commit()
            return novo_categoria
        except (Exception) as e:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='Erro ao salvar, {e}')
                
"""@router.put('/{usuario_id}',
            response_model=UsuariosSchemaBase,
            status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuario_id: int,
                      usuario: UsuarioSchemaUp,
                      db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_up: UsuariosSchemaBase = result.scalars().unique().one_or_none()
        
        if usuario_up:
            if usuario.nome:
                usuario_up.nome = usuario.nome
            if usuario.sobrenome:
                usuario_up.sobrenome = usuario.sobrenome
            if usuario.email:
                usuario_up.email = usuario.email
            if usuario.senha:
                usuario_up.senha = usuario.senha
            if usuario.eh_admin:
                usuario_up.eh_admin = usuario.eh_admin
            await session.commit()
            return usuario_up
        else:
            raise HTTPException(detail="Usuario nao encontrado",
                                status_code=status.HTTP_404_NOT_FOUND)
            
@router.delete('/{usuario_id}', status_code=status.HTTP_404_NOT_FOUND)
async def delete_usuario(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_del: UsuariosSchemaBase = result.scalars().one_or_none()
        
        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Usuario nao encontrado",
                                status_code=status.HTTP_404_NOT_FOUND)"""