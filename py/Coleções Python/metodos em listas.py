lista = [14, 3, 5, 6, 84, 9, 19, 41]

# ==============================================================================
# MÉTODO SORT

lista.sort()  # ordena a lista em ordem crescente

# método não retorna um valor, se dermos print(lista.sort()), a saída sairá None
print(lista)

# ==============================================================================
# MÉTODO COUNT

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

print(lista2.count('e'))  # retorna o nro de ocorrências do valor informado na lista

# ==============================================================================
# MÉTODO APPEND

lista.append(35)  # Adiciona o elemento informado após o último item na lista
# lista.append(35, 48, 93) ===> isto retornará um TypeError, como mostrado abaixo
#     lista.append(35, 48, 93) # ===> isto retornará um TypeError
# TypeError: list.append() takes exactly one argument (3 given)

# Porém se fizermos,
lista.append([35, 48, 93])  # ===> será aceito, porque, uma lista é um tipo de dado

print(lista)
print(lista.append(99))  # o método append não retorna um valor, a saída será None

# ==============================================================================
# MÉTODO EXTEND

lista.extend([2, 45, 7])
# adiciona itens na lista separadamente, cada valor da lista entrará como elemento adicional
print(lista)
# lista.extend(23) ===> não será aceito, extend aceita objetos iteráveis
#     lista.extend(23)
# TypeError: 'int' object is not iterable
lista.extend('geek')  # será aceito, pois uma string é um iterável, e cada letra terá um index diferente
print(lista.extend('loco'))  # Retornará None, porém adicionará a string
print(f'Saída: {lista}')

# ==============================================================================
# MÉTODO INSERT

lista.insert(2, 'novo valor')  # insere item no index 2
# o método insert não substitui valores, descola-os à direita
print(lista)
print(lista.insert(5, 'bla'))  # Retornará None, porem adicionará a string sem separar as letras
print(f'Saída: {lista}')

# ==============================================================================
# MÉTODO REVERSE

lista.reverse()  # ordena a lista do último valor para o primeiro (como o nome diz, reverso)
print(lista)
print(lista.reverse())  # Saída None
print(lista)  # Porém o comando reverse é efetuado mesmo retornando None
# também pode ser feito como abaixo
lista = lista[::-1]  # altera a lista para um lista invertida (mesmo resultado do reverse) porém usando atribuição
print(lista)
print(lista[::-1])  # Retorna a lista invertida, porém não a altera
print(lista)

# ==============================================================================
# MÉTODO COPY

lista2 = lista.copy()  # copia a lista para uma nova lista com os mesmos valores
print(lista2)
print(lista)

# ==============================================================================
# MÉTODO CLEAR

print(lista2)
lista2.clear()  # apaga todos os elementos da lista, deixando-a como uma lista vazia
print(lista2)
