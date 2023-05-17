from core.configs import settings

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class ClienteModel(settings.DBBaseModel):
    __tablename__ = 'cliente'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    telefone = Column(String(50), nullable=True)
    email = Column(String(200), index=True, nullable=False, unique=True)
    cpf = Column(String(50), nullable=True)
    login = Column(String(50), nullable=True)
    senha = Column(String(100), nullable=False)
