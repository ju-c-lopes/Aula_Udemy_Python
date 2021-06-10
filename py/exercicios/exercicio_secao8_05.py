"""
Exercicios Python - Seção 8

5. Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
Sendo que o raio é passado por parâmetro.
V = 4 * π * R³
    __________
        3

"""
from math import pi, pow

print('Este Programa calcula o volume de uma esfera, dado o raio desta esfera\n')

raio = input('Digite o raio da esfera: ')

if raio != '':
    raio = float(raio)
    diametro = raio * 2
else:
    raio = 0


def calcular_volume_esfera(r):
    """
    Dado o raio de uma esfera, a função calcula o volume desta esfera
    a fórmula usada para calular o volume é a seguinte:

        V = 4 * π * R³
            __________
                3
    """
    volume = (4 * pi * pow(r, 3)) / 3
    return volume


print(f'O volume da esfera com diâmetro de {diametro} de medida é: {calcular_volume_esfera(raio):.2f}')
