"""
Este módulo tem o objetivo de forçar uma conversão de string em inteiro assim que o
usuário entra com um valor por input

Utilizando int(input('...')), se o usuário digitar um valor vazio retorna um erro
este módulo visa prevenir esse erro
"""


def toint(n):
    """Converterá a string passada por input para int"""
    if n == '':
        n = 0
    else:
        n = int(n)
    return n


def tofloat(n):
    """Converterá a string passada por input para float"""
    if n == '':
        n = 0
    else:
        n = float(n)
    return n
