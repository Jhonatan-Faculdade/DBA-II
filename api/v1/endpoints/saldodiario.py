from datetime import date
from fastapi import APIRouter
from typing import List
"""from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse"""

from models.saldodiario_model import SaldoDiarioModel

from core.database import connection

router = APIRouter()

@router.get('/', response_model=List[SaldoDiarioModel])
async def get_saldodiarios():
  cursor = connection.cursor(dictionary=True)
  cursor.execute("select * from saldodiario")
  results = cursor.fetchall()
  
  cursor.close()
  connection.close()
  return results

@router.get('/data/{data}', response_model=SaldoDiarioModel)
async def get_saldodata(data: str):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from saldodiario where data = %s", [data])
    result = cursor.fetchone()

    cursor.close()
    # connection.close()
    return result



@router.get('/{saldodiario_data}', response_model=SaldoDiarioModel)
async def get_saldodiarioperiodo(data_inicial: date, data_final: date):
  cursor = connection.cursor(dictionary=True)
  sql=("select * from saldodiario where data BETWEEN %s and %s", (data_inicial , data_final))
  valores = (data_inicial, data_final) 
  
  cursor.execute(sql, valores)
  result = cursor.fetchone()
  
  cursor.close()
  connection.clone()
  return result

