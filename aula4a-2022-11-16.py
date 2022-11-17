#1 passo - Importando a biblioteca sqlite
import sqlite3

#2 passo - Estabelecendo comexão com o banco de dados
conexao = sqlite3.connect('dc_universe.db')

#3 passo - Criar um objeto do tipo cursor
cursor = conexao.cursor()

#4 passo - Comando SQL
sql = 'SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas'

#5 passo - Executar o comando SQL no SQLite (no cursor)
cursor.execute(sql)

#6 passo - Exibir a consulta com todos os nomes de herois e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  
for pessoa in pessoas:
  print(f'Nome: {pessoa[1]} é {pessoa[3]}')