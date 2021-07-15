"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open("texto.txt")

print(arquivo.read())

# seek() -> A função seek() é utiliada para movimentação do cursor pelo arquivo.
# Ela recebe como parâmtro que indica onde queremos colocar o cursor.
# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0)
print(arquivo.read())
arquivo.seek(22)
print(arquivo.read())


arquivo = open("texto.txt")

# print(arquivo.read())

# readline() -> Função que lê o arquivo linha a linha

print(arquivo.readline())
print(arquivo.readline())


arquivo = open("texto.txt")

# readlines() ->

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo, devemos fechar esta conexão. Para isso utilizamos a função close();

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo.

2 - Trabalhar o arquivo.

3 - Fechar o arquivo.

# 1 - Abrir o arquivo.
arquivo = open("texto.txt")
# 2 - Trabalhar o arquivo.
print(arquivo.read())
print(arquivo.closed) # -> Verifica se True se o arquivo está fechado, False se está aberto
# 3 - Fechar o arquivo.
arquivo.close()


arquivo = open("texto.txt")

print(arquivo.read(30)) # -> Limita em 30 caracteres a quantidade que será printada
"""

arquivo = open("texto.txt")

print(arquivo.read(30))  # -> Limita em 30 caracteres a quantidade que será printada
