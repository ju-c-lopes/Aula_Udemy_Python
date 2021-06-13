"""

Exercicios Python - Seção 8

15. Crie um programa que receba três valores (obrigatoriamente maiores que zero), repre-
sentando as medidas dos três lados de um triângulo. Elabore funções para:
    ( a) Determinar se esses lados formam um triângulo, sabendo que:
        • O comprimento de cada lado de um triângulo é menor do que a soma dos outros
        dois lados.
    (b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo.
    Sendo que:
        • Chama-se equilátero o triângulo que tem três lados iguais.
        • Denominam-se isósceles o triângulo que tem o comprimento de dois lados
        iguais.
        • Reoebe o nome de escaleno o triângulo que tem os três lados diferentes.

"""
from convert import tofloat

lado1 = tofloat(input('Lado 1: '))
lado2 = tofloat(input('Lado 2: '))
lado3 = tofloat(input('Lado 3: '))


def formar_triangulo(l1, l2, l3):
    """
    Verifica se os lados informados formam um triângulo
    """
    if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
        return 'Os 3 lados informados formam um triângulo'
    return False


def tipo_triangulo(l1, l2, l3):
    """
    Verifica o tipo de triângulo que é formado pelos lados informados
    """
    if l1 == l2 and l2 == l3:
        return 'triângulo equilátero'
    elif l1 != l2 and l1 != l3 and l2 != l3:
        return 'triângulo escaleno'
    else:
        return 'triângulo isósceles'


ok = formar_triangulo(lado1, lado2, lado3)
if not ok:
    print('Os lados informados não formam um triângulo')
else:
    print(ok)
    print(f'Os lados informados formam um {tipo_triangulo(lado1, lado2, lado3)}')
