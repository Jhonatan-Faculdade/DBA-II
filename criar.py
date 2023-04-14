from config import conexao
from datetime import datetime
from random import randint

cursor = conexao.cursor()

sql = """insert into pessoa 
        (nome, endereco, telefone, celular, 
        email, cpf, cidade, nascimento)
        values
        (%s, %s, %s, %s,
        %s, %s, %s, %s)
      """
      
dados = (
    "Tiburcio Gomes",
    "Entrada Linha XXIV",
    "(46) 3524-2411",
    "(46) 99911-1124",
    "bar_e_48_do_tiburcio@bol.com.br",
    "123.456.789-99",
    randint(1, 5570),
    datetime(1950, 2, 24),   
)

cursor.execute(sql, dados)
conexao.commit()
conexao.rollback() 

pessoaId = cursor.lastrowid

cursor.close()
conexao.close()

print("pessoa inserida com sucesso", pessoaId)