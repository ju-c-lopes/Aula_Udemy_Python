import math
"""
Map

Com Map, fazemos mapeamento de valores para função.

def area(r):
    # "Calcula a área de um círculo com raio 'r'"
    """  # return math.pi * (r ** 2)
"""

# print(area(2))

raios = [2, 5, 7.1, 0.3]

# Forma comum
# areas = []
# for r in raios:
#     areas.append((area(r)))
#
# ou
#
# raios = [2, 5, 9, 13, 44]
# 
# areas = [area(r) for r in raios]
#
# print(areas)

# Forma 2 - Map

# Map é uma função que recebe 2 parâmetros, o primeiro a função, o segundo um iterável
# Retorna um map object

areas = map(area, raios)
print(areas)
print(type(areas))

print(list(areas))

# Forma 3 - Map com lambda

# areas = map(lambda r: math.pi * (r ** 2), raios)
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map, depois da primeira utilização do resultado, ele zera

# Para fixar - Map

# temos dados iteráveis:

# dados: a1, a2, ...., an

# temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)
"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27)]
#
# print(cidades)
#
# # Celsius para Farehneith
#
# # Lambda
#
c_para_f = lambda dado: (dado[0], '{:.2f}'.format((9/5) * dado[1] + 32))

print(list(map(c_para_f, cidades)))


# def area(r):
#     return math.pi * (r ** 2)
#
#
# print(area(2))

# ===========================================================
# raios = [2, 5, 7.1, 0.3]
#
# areas = map(area, raios)

# print(areas)
# lista = list(areas)
# print(lista)

# print(list(map(lambda r: math.pi * (r ** 2), raios)))
