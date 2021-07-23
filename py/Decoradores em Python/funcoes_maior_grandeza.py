"""
Funções de Maior Grandeza - Higher Order Functions = HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter
que retornam outras funções como resultado ou mesmo que podemos passar
funções como argumentos para outras funções, e até mesmo criar variáveis
do tipo de funções nos nossos programas.

OBS: Na seção de funções, nós utilizamos HOF.

Em Python, as funções são cidadãos de primeira classe, First Class Citizen



# Exemplo - Definindo as funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas


# Em Python, podemos também ter funções dentro de funções, que são conhecidas
# por Nested Functions, ou também Inner Functions (Funções Internas

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Angelina'))
print(cumprimento('Felicity'))


# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahaha', 'kkkkkkkk', 'uauauauaua'))
    return rir


# Testando

rindo = faz_me_rir()
print(rindo())

"""

# Inner Functions (Funções internas / Nested Functions) podem acessar o
# escopo de funções mais externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'kkkkkkk', 'lolololol'))
        return f'{risada} {pessoa}'
    return dando_risada


# Testando

rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())

