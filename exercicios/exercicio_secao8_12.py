"""

Exercicios Python - Seção 8

12. Escreva uma função que receba um número inteiro maior do que zero e retorne a soma
de todos os seus algarismos. Por exemplo, ao número 251 oonesponderá o valor 8 (2
+ 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem "Número inválido".

"""

print('\nVamos calcular a soma dos algarismos do número informado')
num = input('Digite o número desejado: ')


def somar_algarismos(n):
    """
    Esta função somará os algarismos de um número informado pelo usuário utilizando o argumento num como parâmetro
    """
    i = len(n)
    algarismos = list(n[::])
    soma = 0
    for a in range(0, i):
        soma = soma + int(algarismos[a])

    return soma


print(f'\nA soma dos algarismos do número {int(num)} é {somar_algarismos(num)}')
