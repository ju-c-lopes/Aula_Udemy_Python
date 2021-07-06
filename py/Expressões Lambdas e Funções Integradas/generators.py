"""
Generator Expression

Em aulas anteriores, estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension.... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# O Generator object descarta os valores após sua utilização, assim como map e filter


# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de
# bytes em memória do elemento passado como parâmetro
# Mostra quantos bytes a string 'Geek" está ocupando em memória.
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(92345668801))
print(getsizeof(True))
"""

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print(' Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp}')
print(f'Set Comprehension: {set_comp}')
print(f'Dictionary Comprehension: {dict_comp}')
print(f'Generator Expression: {gen}')

# Pode iterar no Generator Expression? sim

gene = (x * 10 for x in range(1000))

for num in gene:
    print(num)
