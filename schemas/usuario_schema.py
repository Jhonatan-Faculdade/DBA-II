from typing import Optional
from pydantic import BaseModel, EmailStr

class UsuariosSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        orm_mode = True
    