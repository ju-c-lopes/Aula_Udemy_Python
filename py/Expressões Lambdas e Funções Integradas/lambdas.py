"""
Utilizando Lambdas

Conhecidas por expressões lambdas, ou simplesmente lambdas, são funções sem nome,
ou seja, funções anônimas.

# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))


# Expressão Lambda

# lambda x: 3 * x + 1

# E como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas


q


print(nome_completo(' angelina', 'JOLIE'))

# Em funções Python, podemos ter nenhuma ou várias entradas. Em Lambdas também

amar = lambda: 'Como não amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1/x + 1/y + 1/z)

# n = lambda x1, x2, .... xn <expresão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

#   autores  . |  sort    (   key    |  =  lambda    sobrenome:  |    sobrenome.split(' ')[-1].lower())
#     ^        |   ^           ^     |                   ^       |  # o parametro sobrenome são os elementos da
#     |        |   |           |     |                   |       |  # lista autores (strings de nomes inteiros)
#  variável    | método   <-  param  |    expressão <- param     |  # split divide e [-1] pega o último valor dividido

print(autores)

"""

# Função Quadrática

# f(x) = a * (x ** 2) + (b * x) + c

# Definindo a função


def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c


# teste = geradora_funcao_quadratica(2, 3, -5)
#
# print(teste(0))
# print(teste(1))
# print(teste(2))
print(geradora_funcao_quadratica(2, 3, -5)(2))
