"""
Exercicios Python - Seção 8

3. Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor
de retmno será 1 se positivo, -1 se negativo e O se for igual a 0.
"""
from convert import toint

n = toint(input('Digite um número: '))


def ver_positivo_negativo(num):
    """
    Verifica se o número digitado é positivo ou negativo
    Caso seja um número positivo, retorna 1
    Caso seja um número negativo, retorna -1
    Caso seja zero retorna 0
    """
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0


print(ver_positivo_negativo(n))
