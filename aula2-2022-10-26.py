# comando input(): permitir que o usuario digite algo.
nome = input('Qual seu nome: ')
idade = int(input('Digite sua idade: '))
print(f'Bem-vindo {nome}.')
print(f'Sua idade é {idade} anos')
print(f'O dobro da sua idade é {2 * idade} anos')
genero = input('Qual seu genero? [M/F]').upper()
if genero == 'M':
  if idade == 18:
    print('Você precisar se alistar!')
  elif idade > 18:
    print('Você já passou da idade, se não se alistou procure imediatamente uma unidade do EB.')
  else:
    print('Ainda está muito novo.')
else:
  print('Você não tem precisão de se alistar!.')
