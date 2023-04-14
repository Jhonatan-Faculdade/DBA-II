from random import randint
from config import conexao
from datetime import datetime

cursor = conexao.cursor()

sql = """delete pessoa
        where id = '3' """
        

cursor.execute(sql)
conexao.commit() #inserir e ver os dados
#conexao.rollback() #voltar os dados 

ultimalinha = cursor.rowcount

cursor.close()
conexao.close()

print("Pessoa alterada com sucesso", ultimalinha)