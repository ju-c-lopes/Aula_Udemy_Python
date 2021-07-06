"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos
iteráveis passados como entrada em pares.

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, ou dicionario

print(list(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))
zip1 = zip(lista1, lista2)  # -> ao fazer zip pra dict, ele pede 2 iteraveis, o primeiro será chave, o segundo valor
print(dict(zip1))


# O zip usa como parâmetro o menor iterável, isto significa que se estiver
# trabalhando com iteráveis de tamanhos diferentes, irá para quando os
# elementos do menor iterável acabar.
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
"""

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dic = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dic.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))  # -> asterisco serve para descompactar um iterável

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}  # dictionary comprehension
print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print('\nUtilizando Map:\n')
print(dict(final))


def grade(m):
    return list(map(lambda n: max(n), m))


print(grade(zip(prova1, prova2)))
