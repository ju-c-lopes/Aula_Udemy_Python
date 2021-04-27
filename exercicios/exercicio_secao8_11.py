"""

Exercicios Python - Seção 8

11. Elabore uma função que receba três notas de um aluno como parâmetros e uma letra.
Se a letra for A a função deverá calcular a média aritmética das notas do aluno; se for P,
deverá calcular a média ponderada com pesos 5, 3 e 2.

"""
from convert import tofloat

print('\nQue tipo de média você deseja calcular?\n')
tipo_media = input('Digite A para média aritmética ou P para média ponderada: ')
tipo_media = tipo_media.upper()

print('\n\nDigite as notas a serem calculadas:\n')
nota1 = tofloat(input('Nota 1: '))
nota2 = tofloat(input('Nota 2: '))
nota3 = tofloat(input('Nota 3: '))


def calc_media(n1, n2, n3, t='A'):
    """
    Calculará a média, dado as notas passadas por argumentos
    caso seja a média aritmética, o parâmetro t receberá 'A', que está por padrão,
    caso seja a média ponderada, o parâmetro t receberá 'P'.

    :param n1: nota 1
    :param n2: nota 2
    :param n3: nota 3
    :param t: tipo de média 'A' ou 'P'
    :return: retorna a média calculada
    """
    if t == 'A':
        media = (n1 + n2 + n3) / 3
    else:
        media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / (5 + 3 + 2)

    return media


if tipo_media == 'A':
    t = 'aritmética'
else:
    t = 'ponderada'

print(f'A média {t} é {calc_media(nota1, nota2, nota3, tipo_media):.2f}')
