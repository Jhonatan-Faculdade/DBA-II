from core.configs import settings

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class FormaEntrega(settings.DBBaseModel):
    __tablename__ = 'formas_entrega'

    id = Column(Integer, primary_key=True)
    tipo: str = Column(String(100), nullable=True)