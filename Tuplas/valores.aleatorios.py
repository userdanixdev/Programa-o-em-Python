#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados
#Também indique o menor e o maior valor que estão na tupla.

'''Como irei randomizar valores e colocar em uma tupla?'''

from random import randint  # método de randomizar número inteiros
numbers = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram: ',end='')
for n in numbers:
    print(f'{n} ',end='')
print(f'\nO maior valor sorteado foi: {max(numbers)}')
print(f'O menor valor sorteado foi: {min(numbers)}')