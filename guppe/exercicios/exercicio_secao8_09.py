"""
Exercicios Python - Seção 8

9. Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume
do cilindro. O volume de um cilindm circular é calculado por meio da seguinte fórmula :
V = π * raio² * altura , onde π = 3.141592.
"""
from math import pi
from convert import tofloat

print('\nEste programa calculará o volume do cilindro\n')

altura = tofloat(input('Qual é a altura do cilindro? '))
raio = tofloat(input('Qual é o raio do cilindro? '))


def calc_volume(a, r):
    """
    Esta função calculará o raio do cilindro, dados a altura e o raio informado pelo usuário
    a fórmula é a seguinte

    V = π * raio² * altura
    """
    vol = pi * (r ** 2) * a
    return vol


print(f'O volume do cilindro é {calc_volume(altura, raio):.2f}')
