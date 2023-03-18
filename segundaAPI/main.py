from fastapi import (
    FastAPI, 
    HTTPException, 
    Path, 
    status,
    Response,
    Query,
    Header,
    Depends
)
from typing import List
from models import Curso, cursos


app = FastAPI(
    title="Api de cursos",
    version="1.0.1",
    description="Uma API especial para pessoas especiais"
)

@app.get('/cursos', 
         description="Retorna todos os cursos", 
         summary="Todos os cursos",
         response_model=List[Curso],
         response_description="Deu certo")
async def get_cursos():
    return cursos

@app.get('/curso/{curso_id}',
         response_model=List[Curso])
async def get_curso(curso_id: int = Path(default=None,
                                         gt=0, lt=3)):
    try:
        curso = curso[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso nao encontrado"
        )




if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
    
    