"""
Exercicios Python - Seção 8

2. Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela
no formato textual por extenso. Exemplo: Data: 01 /01 /2000, imprimir: 1 de janeiro de
2000.

"""
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print('Digite a data de hoje\n')

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

mes30 = ['fevereiro', 'abril', 'junho', 'setembro', 'novembro']
bissexto = False
mes2erro = False
mes30erro = False


def converter_data(d, m, a):
    """ Escreve a data informada por escrito """
    if d > 31:
        return 'Dia inválido'
    if m > 12:
        return 'Mês Inválido'

    for i in range(0, 13):

        if m == i:
            m = meses[i - 1]

    ver_mes(d, m, a)
    if mes2erro or mes30erro:
        if mes2erro:
            return 'Mês de fevereiro não tem o dia informado, verifique a data correta'
        elif mes30erro:
            return 'Mês não tem o dia informado, verifique a data correta'
    else:
        return f'{d} de {m} de {a}'


def ver_mes(day, mounth, year):
    global mes30erro
    if mounth in mes30:
        if mounth == 'fevereiro' and day > 28:
            ver_mes2(day, year)
        elif day >= 31:
            mes30erro = True
            return mes30erro


def ver_mes2(day, y):
    global mes2erro
    if day >= 29:
        ver_bissexto(y)
        if day == 29 and bissexto:
            pass
        else:
            mes2erro = True
            return mes2erro


def ver_bissexto(y):
    global bissexto
    if y % 4 == 0:
        bissexto = True
    return bissexto


print(converter_data(dia, mes, ano))
