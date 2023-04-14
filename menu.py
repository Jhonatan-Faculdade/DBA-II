from config import conexao


cursor = conexao.cursor()

print("selecione a consulta")
print("01 - selecionar todas as pessoas que tem mais de 18 anos")
print("02 - selecionar todas as colunas da cidade")
print("03 - selecionar a uf e quantas cidades tem em cada uf")
print("04 - selecionar a pessoa mais velha")
print("05 - selecionar qual a pessoa mais nova")
print("06 - selecionar o nome, endereco, telefone, celular, nome_cidade, nascimento das pessoas que moram no PR")
print("07 - selecionar as cidades possuem pessoas cadastradas e quantas pessoas em cada cidade")
print("08 - selecionar todas as pessoas ativas exibindo todas as colunas ordenando pelo telefone")
print("09 - selecionar todas as cidades que nao possuem pessoas")
print("10 - selecionar quais pessoas tem e-mail do hotmail")

opt=0
opt=int(input(print("Qual opção: ")))



match opt:
    case 1:
        sql="select * from pessoa where nascimento <= DATE_SUB(CURRENT_DATE, INTERVAL 18 YEAR)"
       
    case 2:
        sql="select * from cidade"
        
    case 3:
        sql="""SELECT cidade.UF, COUNT(cidade.id) AS quantidade_de_cidades
        FROM cidade
        GROUP BY cidade.UF;
        """
      
    case 4:
        sql="""SELECT *
        FROM pessoa
        WHERE nascimento IS NOT NULL
        ORDER BY nascimento asc
        limit 1;"""
        
    case 5:
        sql="""SELECT *
        FROM pessoa
        WHERE nascimento IS NOT NULL
        ORDER BY nascimento desc
        limit 1;"""
       
    case 6:
        sql="""select p.id, p.nome, p.endereco, p.telefone, p.celular, p.cidade, p.nascimento
                from pessoa p 
                left outer join cidade c 
                on p.cidade = c.Id 
                where c.Uf = 'PR'"""
     
    case 7:
        sql="""SELECT c.nome AS cidade, COUNT(p.id) AS quantidade_de_pessoas
        FROM cidade c
        INNER JOIN pessoa p ON c.id = p.cidade
        GROUP BY c.nome"""

      
    case 8:
        sql="""select * from pessoa
                where ativo = true
                order by telefone"""
        
    case 9:
        sql="""select c.Id, c.Nome, c.Uf
                from cidade c
                left outer join pessoa p
                on p.cidade = c.id
                where p.id is null"""
        
    case 10:
        sql="""select * from pessoa
                where email like '%@hotmail.com'"""
   
cursor.execute(sql)

resultados = cursor.fetchall()

cursor.close()
conexao.close()

for linha in resultados:
    print(str(linha))
    print('--------------------------------------')        