"""
Exercicios Python - Seção 8

1. Crie uma função que recebe como parâmetro um número inteiro e devolve o seu dobro.
"""
from convert import toint

N = toint(input('Digite um número inteiro: '))


def dobrar(num):
    """ Dobra o número informado pelo usuário """
    return num * 2


print('\n')
print(f'O dobro do número que você indicou é {dobrar(N)}')
