import statistics
# Biblioteca para trabalhar com dados estatísticos

"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção


"""

# valores = 1, 2, 3, 4, 5, 6
#
# media = (sum(valores) / len(valores))
#
# print(media)

# Exemplo: Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

# OBS: Assim como a função map(), a filter recebe dois parâmetros, sendo uma
# função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))
print(list(res))

# Assim como na função map(), após serem utilizados dos dados de filter(),
# ele são excluídos da memória

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', 'Peru', '', '', 'Bolivia']

filtro = filter(None, paises)  # filtrará a lista paises tirando os dados vazios

print(list(filtro))

fil = filter(lambda pais: pais != '', paises)
filt = filter(lambda pais: len(pais) > 0, paises)

print(list(fil))

# Filter requer 2 parâmetros

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Hoje vou sair"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter
# FORMA 1
# inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
# print(inativos)

# FORMA 2
# vazio significa False comparando com bool
# inativos = list(filter(lambda user: not user['tweets'], usuarios))
# print(inativos)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria', 'Deia']

# Devemos criar uma lista contendo "Sua instrutora é" + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
#             ^                                                ^        ^       ^       ^
#             |         <-                     <-              |        |       |       |
#
# O filter() acíma é usado como o parâmetro iterável da função map
print(lista)
