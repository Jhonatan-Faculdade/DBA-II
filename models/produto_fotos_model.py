from pymysql import Timestamp
from sqlalchemy import Column, ForeignKey, Integer, String
from core.configs import settings

class ProdutoFotos(settings.DBBaseModel):
   __tablename__ = 'produto_fotos'
   
   id = Column(Integer, primary_key=True, autoincrement=True)
   produto_id = Column(Integer, ForeignKey('produto.id'))
   url = Column(String(100))
   descricao = Column(String(30))
   data = Column(Timestamp)