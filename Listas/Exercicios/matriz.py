# Crie um programa que declare uma matriz de dimensão 3×3 e preencha
# com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
# Fazer um laço de repetição para preencher tanto as linhas logo as colunas:
for linha in range(0,3):
  for coluna in range(0,3):
    matriz[linha][coluna]=int(input(f'Digite um valor para [{linha},{coluna}]: ')
print('='*30)
# SEGUNDA PARTE:
    # Mostrar a estrutura na tela -> Outro duplo laço :
for linha in range(0,3):
  for coluna in range(0,3):
    print(f'[{matriz[linha][coluna]:^5}]',end='')
  print()
  
