"""
Exercicios Python - Seção 8

6. Faça uma função que receba 3 númemos inteiros como parâmetro, representando horas,
minutos e segundos, e os converta em segundos.
"""

hora = input('Digite a hora: ')
if hora == '':
    hora = 0
else:
    hora = int(hora)

minuto = input('Digite os minutos: ')
if minuto == '':
    minuto = 0
else:
    minuto = int(minuto)

segundo = input('Digite os segundos: ')
if segundo == '':
    segundo = 0
else:
    segundo = int(segundo)


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
