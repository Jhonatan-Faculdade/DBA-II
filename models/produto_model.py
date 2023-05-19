<<<<<<< HEAD
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import relationship
from core.configs import Settings


class ProdutoModel(Settings.DBBaseModel):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(Text)
    preco = Column(Numeric(15, 2))
    fracionado = Column(Boolean, default=False)
    avaliacao = Column(SmallInteger, default=5)
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'))
    restaurante = relationship("RestauranteModel", back_populates='produtos', lazy='joined')
    tamanho = Column(String(5))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship("CategoriaModel", back_populates='produtos', lazy='joined')
=======
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text, Boolean, SmallInteger
from sqlalchemy.orm import relationship
from core.configs import settings

class ProdutoModel(settings.DBBaseModel):
   __tablename__ = 'produtos'
   
   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(150), nullable=True)
   descricao = Column(Text)
   preco = Column(Numeric(15,2))
   fracionado = Column(Boolean, default=False)
   avaliacao = Column(SmallInteger, default=5)
   tamanho = Column(String(5))
   categoria_id = Column(Integer, ForeignKey('categoria.id'))
   categoria = relationship("CategoriaModel", back_populates='produtos', lazy='joined')
>>>>>>> ccc132a80a70250c0b6e32c20b03c863ff38c16a
