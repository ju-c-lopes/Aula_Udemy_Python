"""

Exercicios Python - Seção 8

14. Faça uma função que receba a distância em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
mensagem de acordo com a tabela abaixo :
        ___________________________________________
        |  CONSUMO  |  (Km/l)  |     MENSAGEM     |
        | menor que |    8     |  Venda o carro!  |
        |   entre   |  8 e 14  |     Econômico!   |
        | maior que |    12    | Super econômico! |
        -------------------------------------------
"""
from convert import toint

distancia = toint(input('Qual a distância percorrida? '))
litros_gastos = toint(input('Quantos litros de gasolina foram gastos? '))

consumo = distancia / litros_gastos


def ver_eficiencia(c):
    """
    Função que calcula a eficiência de um veículo para uma análise de compra e venda
    """
    if c <= 8:
        return 'Venda o carro!'
    elif 8 < c < 14:
        return 'Econômico!'
    else:
        return 'Super econômico!'


print(f'O carro faz {consumo} km/l\n')
print(ver_eficiencia(consumo))
