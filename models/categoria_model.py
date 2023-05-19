from sqlalchemy.orm import relationship
from core.configs import settings

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class CategoriaModel(settings.DBBaseModel):
<<<<<<< HEAD
    __tablename__ = 'categorias'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    descricao: str = Column(String(100))
    icone: str = Column(String(200))
    eh_ativa: bool = Column(Boolean)
    produtos = relationship(
        "CategoriaModel", cascade="all, delete-orphan",
        back_populates='categoria',
        uselist=True,
        lazy="joined"
    )
=======
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(100), nullable=False)
    icone = Column(String(300), nullable=True)
    ativa = Column(Boolean, default=True)
    produtos = relationship("CategoriaModel", 
                            cascade="all, delete-orphan", 
                            back_populates='categoria', 
                            uselist=True, 
                            lazy="joined")
>>>>>>> ccc132a80a70250c0b6e32c20b03c863ff38c16a
