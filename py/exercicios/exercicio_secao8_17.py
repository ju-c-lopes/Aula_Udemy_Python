"""

Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a
soma dos N números inteiros existentes entre eles.

"""


def between_sum(x, y):
    """
    Esta função fará a soma dos números entre os 2 números informados

    :param x: número inicial
    :param y: número final
    :return: soma final
    """
    soma = 0
    for i in range(x, y + 1):
        soma = soma + i
    return soma


print(between_sum(2, 7))
