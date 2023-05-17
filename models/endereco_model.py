from sqlalchemy import Column, Float, ForeignKey, Integer, String
from core.configs import settings
from sqlalchemy.orm import relationship


class Endereco(settings.DBBaseModel):
    __tablename__ = 'enderecos'

    id: int = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    rua: str = Column(String(50), nullable=True)
    numero: str = Column(String(50), nullable=True)
    bairro: str = Column(String(50), nullable=True)
    cidade: str = Column(String(50), nullable=True)
    cep: str = Column(String(50), nullable=True)
    referencia: str = Column(String(50), nullable=True)
    latitude: Float = Column(Float(50), nullable=True)
    longitude: Float = Column(Float(50), nullable=True)

    cliente = relationship("Cliente", back_populates="enderecos")