"""
Exercicios Python - Seção 8

4. Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado
perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de
outro número inteiro . Ex : 1, 4, 9 ...

"""

from math import sqrt
import convert

n = convert.toint(input('Digite um número: '))


def ver_quadrado_perfeito(num):
    
    if num == (sqrt(num) * sqrt(num)):
        return f'O número {num} é um quadrado perfeito'
    return f'O número {num} não é um quadrado perfeito'


print(ver_quadrado_perfeito(n))
