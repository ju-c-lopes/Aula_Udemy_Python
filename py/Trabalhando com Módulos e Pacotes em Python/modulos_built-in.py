"""
Trabalhando com Módulos Built-in (módulos integrados, que já vem instalados no Python)

________________________
|Python|Módulos builtin|
------------------------


# import random

# print(random.random()) --> versão completa


# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())
# print(random.random()) --> lançaria um erro pois apelidamos random como rdm


# Podemos importar todas as funções de um módulo utilizando o *
from random import *

print(random())

# Importando todo o módulo
import random
print(random.random())


# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))


https://docs.python.org/3/py-modindex.html
"""

# Costumamos a utilizar tuple para colocar múltiples imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
