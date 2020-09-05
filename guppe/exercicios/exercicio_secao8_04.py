"""
Exercicios Python - Seção 8

4. Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado
perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de
outro número inteiro . Ex : 1, 4, 9 ...

"""

from math import sqrt

n = input('Digite um número: ')
n = int(n)


def ver_quadrado_perfeito(num):
    print(num)
    if num == (sqrt(num) * sqrt(num)):
        return f'O número {num} é um quadrado perfeito'
    return f'O número {num} não é um quadrado perfeito'


print(ver_quadrado_perfeito(n))
