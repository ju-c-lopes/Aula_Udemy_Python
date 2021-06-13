"""
Módulo Collections - Named Tuple

# Recap Tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também parametros
"""

# Import
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named TUple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)
print(type(ray))

print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)
