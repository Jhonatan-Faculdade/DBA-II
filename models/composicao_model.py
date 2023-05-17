from core.configs import settings

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship


class ComposicaoModel(settings.DBBaseModel):
    __tablename__ = 'composicao'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    produto_id = Column(Integer, ForeignKey('produto.id'))
    produto = relationship("ProdutoModel", back_populates='composicao', lazy='joined')
    descricao: str = Column(String(100))
    preco = Column(Numeric(15, 2))
    