"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

no Python:
True => Verdadeiro
False => Falso

OBS: Sempre com a inicial maiúscula

Errado: true, false

Certo: True, False
"""

ativo = True
print(f'Imprimindo valor e tipo da variável booleana ativo ===> valor: {ativo}')
print(type(ativo))

ativo = False
print(f'Imprimindo valor e tipo da variável booleana ativo ===> valor: {ativo}')
print(type(ativo))

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso
se for falso, o resultado será verdadeiro, ou seja, sempre o contrário
"""
print('\nImprimindo uma negação(not)\n')
print(not ativo)

logado = True

# ou (or):
"""
É uma operação binária, ou seja,
depende de dois valores, ou um ou outro deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(f'\nImprimindo valor binário (OU->or) entre ativo e logado \n===> valor ativo: {ativo} / valor logado: {logado}')
print('\nativo or logado = {}'.format(ativo or logado))

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
