from core.configs import settings

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class PedidoProduto(settings.DBBaseModel):
    __tablename__ = 'pedido_produtos'

    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'), primary_key=True)
    quantidade: int = Column(Integer)
    valor: Float = Column(Float)
    composicao_id = Column(Integer, ForeignKey('composicao.id'))

    produto = relationship("Produto")
    pedido = relationship("Pedido")
    composicao = relationship("Composicao")
