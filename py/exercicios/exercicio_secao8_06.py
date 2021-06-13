"""
Exercicios Python - Seção 8

6. Faça uma função que receba 3 númemos inteiros como parâmetro, representando horas,
minutos e segundos, e os converta em segundos.
"""
from convert import toint

hora = toint(input('Digite a hora: '))
minuto = toint(input('Digite os minutos: '))
segundo = toint(input('Digite os segundos: '))


def converter_segundos(h, m, s):
    """
    Esta função converterá o horário informado num acumulado de segundos,
    ou seja, informará quantos segundos tem no horário informado.
    """
    conv_hora = h * 60
    sum_min = conv_hora + m
    conv_min = sum_min * 60
    tot_seg = conv_min + s
    return tot_seg


print(f'O horário de {hora}:{minuto}:{segundo}, informado pelo usuário é de '
      f'{converter_segundos(hora, minuto, segundo)} segundos')
