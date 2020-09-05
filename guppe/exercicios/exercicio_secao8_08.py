"""
Exercicios Python - Seção 8

8. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = √ a² + b² . Faça uma função que receba os valores de a e b e calcule o
valor da hipotenusa através da equação.
"""
from math import sqrt

print('\nEste programa tem a função de calcular a hipotenusa através de seus catetos\n')

cateto_A = input('Digite o cateto A: ')
if cateto_A == '':
    cateto_A = 0
else:
    cateto_A = float(cateto_A)

cateto_B = input('Digite o cateto B: ')
if cateto_B == '':
    cateto_B = 0
else:
    cateto_B = float(cateto_B)


def calc_hipotenusa(a, b):
    """
    Calculará o valor da hipotenusa, utilizando os valores dos catetos
    informados pelo usuário.

    A fórmula é a seguinte:

    hipotenusa = √(a² + b²)
    """
    hip = sqrt(a ** 2 + b ** 2)
    return hip


print(f'O valor da hipotenusa é {calc_hipotenusa(cateto_A, cateto_B):.2f}')
