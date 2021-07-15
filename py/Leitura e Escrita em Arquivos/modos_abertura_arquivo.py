"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError.
a -> Abre para escrita adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização. Leitura e escrita.

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado.
Caso exista, o novo conteúdo será adicionado ao final do arquivo. Com o
modo 'a', não controlamos o cursor.

# Exemplo 'x'

try:
    with open("university.txt", 'x') as arquivo:
        arquivo.write("Teste de conteudo.\n")
except FileExistsError:
    print("Arquivo já existe")

# Exemplo 'a'

with open("frutas.txt", 'a') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou sair")
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


https://docs.python.org/3/library/functions.html#open
"""

with open("outro.txt", 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write("rao.\n")
    arquivo.write("Nnha.\n")
    arquivo.write("Mma linha.\n")
