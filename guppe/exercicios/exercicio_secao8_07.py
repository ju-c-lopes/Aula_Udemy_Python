"""
Exercicios Python - Seção 8

7. Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida
em graus Fahrenheit. A fórmula de conversão é : F = C * (9.0/ 5.O) + 32.0, sendo F a
temperatura em Fahrenheit e C a temperatura em Celsius.

"""

celsius = input('Digite a temperaatura em Celsius: ')
if celsius == '':
    celsius = 0
else:
    celsius = float(celsius)


def celsius_to_fahrenheit(c):
    """ Esta função converterá a temperatura de Celsius para Fahrenheit """
    fahr = c * (9.0 / 5.0) + 32
    return fahr


print(f'{celsius}° C são {celsius_to_fahrenheit(celsius):.2f}° F')
