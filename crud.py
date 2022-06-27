import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='',
    password='',
    database='copa22',
)
cursor = conexao.cursor()

#Create

 nome_selecao = "Honduras"
 ranking_fifa = 90
 comando = f'INSERT INTO classificados (nome_selecao, ranking_fifa) VALUES ("{nome_selecao}", {ranking_fifa}) '
 cursor.execute(comando)
 conexao.commit()
 resultado = cursor.fetchall() # ler banco de dados

#Read

 comando = f'SELECT * FROM classificados'
 cursor.execute(comando)
 resultado = cursor.fetchall() # ler banco de dados
 print(resultado)

#Update

 nome_selecao = "Belgica"
 ranking_fifa = 2
 comando = f'UPDATE classificados SET ranking_fifa = {ranking_fifa} WHERE nome_selecao = "{nome_selecao}"'
 cursor.execute(comando)
 conexao.commit()

#Delete

 nome_selecao = "Honduras"
 comando = f'DELETE FROM classificados WHERE nome_selecao= "{nome_selecao}"'
 cursor.execute(comando)
 conexao.commit()


cursor.close()
conexao.close()