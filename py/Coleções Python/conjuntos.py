"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia à Teoria dos conjuntos da matemática

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) Não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas
não nos importamos com a ordenação deles. Quando não precisamos se preocupar com
chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

diferença entre conjuntos (sets) e mapas (dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s= set({1, 2, 3, 4, 5, 5, 6, 7, 3, 2})  # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5,5}
print(s)
print(type(s))

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 12, 1, 44, 5, 2, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como to do outro conjunto Python, podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)


# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu,
# e os visitantes informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em um lista podemos
# adicionar novos elementos e ter repetição

cidades = ['Belo horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(set(cidades))
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
print(s)

# Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Não é indice, informamos o valor a ser removido
print(s)

# Caso o valor não seja encontrado, será gerado erro KeuError

# Forma 2
s.discard(2)
print(s)

# Se o valor não for encontrado, nenhum erro é gerado

# Copiando um conjunto para outro...

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java

estudantes_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
estudantes_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}

# Veja que alguns alunos que estudam python tambem estudam java

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utiliando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando Intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utlizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""


