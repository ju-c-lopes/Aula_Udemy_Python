"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.5'
Ou seja, está entre aspas simples é uma string
como nos exemplos acima, vemos tipo int, bool, float, MAS...eles estão entre aspas simples
Logo, são do tipo string, mesmo que pareçam de outro tipo

- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.5"
OBS: mesmos conceitos da aspas simples

- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.5'''
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.5"""
"""
O Python trabalha com string da seguinte forma (ilustração):
Abaixo vemos que a string 'Agua Viva' é tratada como uma lista de string, que tem as posições conforme ilustrado
[ 0,   1,   2,   3,   4,   5,   6,   7,   8 ]
['A', 'g', 'u', 'a', ' ', 'V', 'i', 'v', 'a']
acima, o Python pega a string e converte em uma lista de string, pegando cada letra individualmente
é a forma como o Python trata string

se fizermos:
nome = 'Agua Viva'
print(nome[0:4])

imprimiremos somente a primeira palavra da string, lembrando que o 4 de(nome[0:4]) ele nao contará,
no caso:
print(nome[5:8]) ele imprimiria --> Viv (sem o ultimo 'a')
precisamos então:
print(nome[5:9]) para imprimir --> Viva

O nome dado a essa operação é: Slice de string
"""


print("comando: nome = 'Geek University'\nresultado: ")
nome = 'Geek University'
print("comando: print(nome)\nresultado: ", end="")
print(nome)
print("comando: print(type(nome))\nresultado: ", end="")
print(type(nome))

# Quando a string precisa ter apóstrofo (') invertemos o tipo de aspas
print('''\ncomando: nome = "Gina's University"\nresultado: ''')
nome = "Gina's University"
print("comando: print(nome)\nresultado: ", end="")
print(nome)
print("comando: print(type(nome))\nresultado: ", end="")
print(type(nome))

""" Para quebra de linha (tipo dar Enter) usamos \n 
Porém o Python aceita fazer da forma como está abaixo
"""

name = '''Angelina
Jolie'''

""" O Python imprimirá como se tivesse dado enter normalmente, 
porém é preciso usar sempre aspas triplas, só testar
"""
print(name)
print(type(name))

"""
A barra invertida \\ pode ser usada como caractere de escape,
usada para permitir o uso de aspas no dentro da string
"""

name = "Angelina \" Jolie "
print(name)

name = 'Angelina Jolie'
print(name.upper())
print(name.lower())
print(name.split())

nome = 'Agua Viva'
print(nome[0:4])
print(nome[5:9])

# [::-1] -> pede para ler do primeiro elemento (:) até o ultimo elemento (:) e depois inverter (-1)
print(nome[::-1])

print(nome.replace('a', 'X'))

# Finalizando:

nome = 'subino onibus'  # é um palindromo
print(nome)
print(nome[::-1])
