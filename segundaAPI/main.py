from fastapi import FastAPI
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
    return cursos;


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
    
    