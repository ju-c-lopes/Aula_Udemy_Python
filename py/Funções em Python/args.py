"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer
coisa, desde que comece com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada
em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 2)  # TypeError

# print(soma_todos_numeros(4, 6, 9, 5))  # TypeError


# Entendendo o *args


def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 4, 7, 9))


# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3,145))
"""


def soma_todos_numeros(*args):
    print(args)
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1, 3, 4, 7))

# numeros = [1, 3, 6, 8]

# print(soma_todos_numeros(numeros))  # TypeError: unsupported operand type(s) for +: 'int' and 'list'

numeros = [1, 3, 6, 8]

num1, num2, num3, num4 = numeros

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterico serve para que informemos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá que
# precisará antes desempacotar estes dados.
