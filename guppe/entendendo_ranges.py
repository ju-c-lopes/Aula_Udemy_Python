"""
Ranges

-> Precisamos conhecer o loop for para usar os rnanges.
-> Precisamos conhecer o range para trabalhor melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada

Formas gerais:

# Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo de 1 em 1)

# Exemplo forma 2
for num in range(4, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(5, 50, 5):
    print(num)

# Forma 4 (inversa, ou de decremento)

range(valor_de_inicio, valor_de_paarada, passo)

OBS: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 4

for num in range(10, 0, -1):
    print(num)
"""


