from core.configs import settings

from sqlalchemy import Column, Integer, String, Boolean

class CategoriaModel(settings.DBBaseModel):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(100), nullable=False)
    icone = Column(String(200), nullable=True)
    ativa = Column(Boolean, default=True)