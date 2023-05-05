from sqlalchemy.orm import relationship
from core.configs import settings

from sqlalchemy import Column, Integer, String, Boolean

class CategoriaModel(settings.DBBaseModel):
   __tablename__ = 'categoria'

   id = Column(Integer, primary_key=True, autoincrement=True)
   descricao = Column(String(100), nullable=False)
   icone = Column(String(300), nullable=True)
   ativa = Column(Boolean, default=True)
   produtos = relationship("CategoriaModel", 
                           cascade="all, delete-orphan", 
                           back_populates='categoria', 
                           uselist=True, 
                           lazy="joined")