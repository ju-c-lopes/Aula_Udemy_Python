"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez, quando uma função next() é chamada.

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.


OBS: Um iterable pode ser transformado em um iterator utilizando a função iter()




nome = 'Geek'  # -> é um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # -> é um iterable mas não é um iterator

# print(next(nome))  # Erro -> 'str' object is not an iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
"""

nome = 'Geek'

for letra in nome:
    # Por debaixo dos panos
    # O Python transforma nome com iter()
    # e dá o comando print(next(nome)) até o último elemento
    print(f'{letra}')

