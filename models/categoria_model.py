<<<<<<< HEAD
from sqlalchemy.orm import relationship
=======
>>>>>>> 832ce3b2250a9447fa443bbb9906a723e922956f
from core.configs import settings

from sqlalchemy import Column, Integer, String, Boolean

class CategoriaModel(settings.DBBaseModel):
<<<<<<< HEAD
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
=======
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(100), nullable=False)
    icone = Column(String(200), nullable=True)
    ativa = Column(Boolean, default=True)
>>>>>>> 832ce3b2250a9447fa443bbb9906a723e922956f
