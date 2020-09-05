"""
Exercicios Python - Seção 8

1. Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.
"""

N = input('Digite um número inteiro: ')

if N == '':
    N = 0
else:
    N = int(N)


def dobrar(num):
    """ Dobra o número informado pelo usuário """
    return num * 2


print('\n')
print(f'O dobro do número que você indicou é {dobrar(N)}')
