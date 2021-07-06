"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela
execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você
escreveu algo que o Python não reconhece como parte da linguagem.

Exemplos SyntaxError

a)

def func:
    print("Geek University")

b)
def = 1

c)
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

# Exemplos NameError

a)
print(geek)

b)
geek()

c)
a = 18

if a < 10:
    msg = 'menor que 10'

print(msg)


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a)
print(len(5))

b)
print('Geek' + [])
print('Geek' + 4)


4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou
outro tipo de dado indexado utilizando um indice inválido

a)
lista = ['Geek']
print(lista[2])
print(lista[0][10])


5 - ValueError -> Ocorre quando uma função/operação built-in (integrado)
recebe um argumento com tipo correto mas valor inapropriado

a)
print(int('Geek'))
print(float('Geek'))


6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

a)
dic = {'python': 'university'}
print(dic['geek'])


7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

a)
def nova():
print('geek')

b)
for i in range(10):
i = i + 1


OBS: Exceptions e Erros são sinônimos na programação.

OBS: Importante ler e prestar atenção na saída de erro.
"""

