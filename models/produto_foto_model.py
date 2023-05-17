from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from core.configs import settings
from sqlalchemy.orm import relationship


class ProdutoFotos(settings.DBBaseModel):
   __tablename__ = 'produto_fotos'
   
   id = Column(Integer, primary_key=True, autoincrement=True)
   produto_id = Column(Integer, ForeignKey('produto.id'))
   produto = relationship("ProdutoModel", back_populates='produtos_foto', lazy='joined')
   url = Column(String(100))
   descricao = Column(String(30))
   data = Column(TIMESTAMP)
