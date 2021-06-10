"""
Funções com parâmetro padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Geek University')

print()


# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())  # TypeError

def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potência insformada pelo usuário

# OBS: Se o usuário passar somente 1 argumento, este será atribuido ao parâmetro número,
# e será calculado o quadrado desde número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro número e o segundo ao parâmetro potência.
# Então será calculada essa potência.

print(exponencial())

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(num=2, potencia):  # os parâmetros devem ser na ordem: não-padrão, depois padrão, contrário ao exemplo
    return num ** potencia


print(teste(6))

# Outros exemplos


def soma(num1=2, num2=5):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError

# Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))

# Porque ustilizar parâmetros com valor default?

- Nos permite ser mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dade:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

# Exemplos utilizando funções como parâmetros


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(3, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# variáveis globais
# variáveis locais

instrutor = 'Geek'  # variável global


def diz_oi():
    instrutor = 'Python'  # variável local (se sobrepoe a variável global)
    return f'Oi {instrutor}'


print(diz_oi())

def diz_oi():
    prof = 'Geek'  # variável local
    return f'olá {prof}'


print(diz_oi())

print(prof)  # NameError


# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0


def incrementa():
    total = total + 1  # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter
                       # sido inicializada)
    return total


print(incrementa())

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())


# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma
# especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

print(dentro())  # NameError
"""



