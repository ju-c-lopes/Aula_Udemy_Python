"""
Tipo Float

Também conhecido como tipo real ou decimal

casas, decimais (ou melhor, casas depois da vírgula)

O separador de casas decimais é o ponto"." e não a virgula","

===>ERRADO
valor = 1,44

===>CERTO
valor = 1.44
"""
# Errado do ponto de vista float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# Podemos converter um float para int
"""
OBS: Ao converter valores float para int, perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
var = 5j
print(type(var))