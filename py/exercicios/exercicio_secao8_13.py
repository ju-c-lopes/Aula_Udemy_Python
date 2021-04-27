"""

Exercicios Python - Seção 8

13. Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo repre-
sentará a operação que se deseja efetuar com os números. Se o símbolo for + deverá
ser realizada uma adição, se for - uma subtração, se for / uma divisão e se for * será
efetuada uma multiplicação.

"""
from convert import tofloat

print('\nQue operação deseja realizar?\n')
operacao = input('Para soma, digite "+"\n'
                 'Para subtração, digite "-"\n'
                 'Para multiplicação, digite "*"\n'
                 'Para divisão, digite "/"\n')

op = ''

if operacao == '+':
    op = 'soma'
elif operacao == '-':
    op = 'subtração'
elif operacao == '*':
    op = 'multiplicação'
elif operacao == '/':
    op = 'divisão'
else:
    print('Operador inválido! Verifique as opções corretamente')
    exit()

print(f'\n\nQuais os números que você deseja efetuar a {op}?\n')
num1 = tofloat(input('Primeiro número: '))
num2 = tofloat(input('Segundo número: '))


def calcular(n1, n2, operador):
    """
    Esta função realiza uma conta, sendo o tipo de conta escolhida pelo usuário
    que posteriormente informará os números a serem calculados

    :param n1: Primeiro número informado pelo usuário e recebido como parâmetro
    :param n2: Segundo número informado pelo usuário e recebido como parâmetro
    :param operador: Símbolo que indicará o tipo de operação a ser realizada
    :return: Cálculo final
    """
    if operador == '+':
        calc = n1 + n2
    elif operador == '-':
        calc = n1 - n2
    elif operador == '*':
        calc = n1 * n2
    else:
        calc = n1 / n2

    return calc


print(f'\nO cálculo da {op} dos números informados é {calcular(num1, num2, operacao):.1f}')
