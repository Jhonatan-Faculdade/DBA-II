from config import conexao

print('Conectado no banco de dados, pia bagual')

sql = "select * from cidade"
cursor = conexao.cursor()

cursor.execute(sql)

resultados = cursor.fetchall()

cursor.close()
conexao.close()

for linha in resultados:
    print(str(linha[0]) + '\t' + linha[1] + '\t' + str(linha[2]))
    print('--------------------------------------')