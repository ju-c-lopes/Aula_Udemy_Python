"""
Módulo Collections - Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida.

# Fazendo o import
from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave} : valor={valor}')

# Ordered Dict é um dicionário que nos garante a ordem de inserção dos elementos

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True/False??? --> True, já que a ordem dos elementos não importa para o dicionário

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # True/False??? --> False, já que a ordem dos elementos importa para o Ordered Dict
"""

# Fazendo o import
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True/False??? --> True, já que a ordem dos elementos não importa para o dicionário

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # True/False??? --> False, já que a ordem dos elementos importa para o Ordered Dict
