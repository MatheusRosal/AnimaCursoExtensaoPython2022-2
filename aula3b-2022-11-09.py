#criação de funções
preco = 1999.90

#calcular 5% de imposto e guarda em uma variavel

imposto = (5/100) * preco
print(imposto)
preco2 = 100
imposto2 = 5/100 * preco2
print(imposto2)

#criar uma função calcular_imposto() que calcula um imposto de 5 % e retorna a quem pediu...
#Isso é a declaração da função
def calcular_imposto(preco_produto):
  imposto = 7/100 * preco_produto
  return imposto

#Aqui é o uso
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

#Explicação de variável x global
print(preco)
preco_produto = 100
print(preco_produto)

#agora calcular imposto a 7%

valores = [1.99, 24.50, 78.27, 1515.5]
#se eu quiser calcular o imposto destes quatro valores e exibir na tela

for c in valores:
  print(f'O imposto de {c} é {calcular_imposto(c)}')

#Declarar um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

#e se o imposto for 10%?
for valor in valores:
  print(f'O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}')