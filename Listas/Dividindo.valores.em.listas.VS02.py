### --- Dividindo valores em listas ---- ###

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares
#e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

# VERSÃO 02 - 

valores=list()
pares=list()
impar=list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp=input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp in 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print(f'''
Lista de valores digitados:{valores}
Lista de valores pares:{pares}
Lista de valores impares:{impar}''')
===========================================================================
Resultados:

Digite um valor: 15
Quer continuar? [S/N]: s
Digite um valor: 15
Quer continuar? [S/N]: x
Digite um valor: 20
Quer continuar? [S/N]: s
Digite um valor: 25
Quer continuar? [S/N]: n

Lista de valores digitados:[15, 15, 20, 25]
Lista de valores pares:[20]
Lista de valores impares:[15, 15, 25]

======================================================

