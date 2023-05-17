from pymysql import TIMESTAMP
from core.configs import settings

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Pedido(settings.DBBaseModel):
    __tablename__ = 'pedido'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'))
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    formas_id = Column(Integer, ForeignKey('formas_entrega.id'))
    formas_de_entrega_id = Column(Integer, ForeignKey('formas_de_entrega.id'))
    endereco_id = Column(Integer, ForeignKey('enderecos.id'))
    data= Column(TIMESTAMP)
    observacao = Column(String)
    status = Column(String)

    restaurante = relationship("Restaurante")
    cliente = relationship("Cliente")
    formas_de_entrega = relationship("FormaEntrega")
    endereco = relationship("Endereco")