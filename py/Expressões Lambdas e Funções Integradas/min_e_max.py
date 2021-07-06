"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 4, 8, 99, 324, 129]
print(max(lista))  # 324

tupla = (1, 4, 8, 99, 324, 129)
print(max(tupla))  # 324

conjunto = {1, 4, 8, 99, 324, 129}
print(max(conjunto))  # 324

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 99, 'e': 324, 'f': 129}
print(max(dicionario))  # f

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 99, 'e': 324, 'f': 129}
print(max(dicionario.values()))  # 324

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))

print(max(val1, val2))

print(max(4, 12, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.7689))

print(max('Geek University'))


min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

# Exemplos

lista = [1, 4, 8, 99, 324, 129]
print(min(lista))  # 324

tupla = (1, 4, 8, 99, 324, 129)
print(min(tupla))  # 324

conjunto = {1, 4, 8, 99, 324, 129}
print(min(conjunto))  # 324

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 99, 'e': 324, 'f': 129}
print(min(dicionario))  # f

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 99, 'e': 324, 'f': 129}
print(min(dicionario.values()))  # 324

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))

print(min(val1, val2))

print(min(4, 12, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.7689))

print(min('Geek University'))  # mostrará o espaço como menor pois ele é o de menor valor e faz parte da string

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim

"""
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Unforgiven", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! imprima somente o título da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Desafio! Como encontrar a musica mais tocada e a menos tocada sem usar max min e lambda

mais = 0
for musica in musicas:
    if musica['tocou'] > mais:
        mais = musica['tocou']

for musica in musicas:
    if musica['tocou'] == mais:
        print(musica['titulo'])


menos = 999
for musica in musicas:
    if musica['tocou'] < menos:
        menos = musica['tocou']

for musica in musicas:
    if musica['tocou'] == menos:
        print(musica['titulo'])
