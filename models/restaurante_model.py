from sqlalchemy import Column, ForeignKey, Integer, Numeric, SmallInteger, String, TIMESTAMP
from sqlalchemy.orm import relationship
from core.configs import settings

class RestauranteModel(settings.DBBaseModel):
   __tablename__ = 'restaurante'
   
   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(150), nullable=False)
   endereco = Column(String(150), nullable=False)
   telefone = Column(String(50), nullable=True)
   avaliacao = Column(SmallInteger, default=5)
   valorMinimo = Column(Numeric(15,2))
   horariosFuncionamento = Column(TIMESTAMP)
   formaEntrega = Column(String(30), nullable=True)
   formaPagamento = Column(String(30), nullable=True)
   categorias = Column(String(50), nullable=True)