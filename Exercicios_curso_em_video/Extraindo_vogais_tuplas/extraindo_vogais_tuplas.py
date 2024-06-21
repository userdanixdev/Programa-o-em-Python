# Extraindo vogais de uma tupla

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Versão 01:

palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar'
            'trabalhar','mercado','programador','futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' /')

