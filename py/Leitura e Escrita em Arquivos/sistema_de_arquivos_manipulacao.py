"""
Sistema de Arquivos - Manipulação


import os

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists("arquivo.txt"))  # False
print(os.path.exists("frutas.txt"))  # True

# Diretório

# Paths relativos
print(os.path.exists('newdir'))  # True
print(os.path.exists('outro'))  # False

# Paths absolutos

print(os.path.exists("/home/juclops/Documents"))  # True
print(os.path.exists("/home/juclops/MeuDiretorio"))  # False


# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()  # este comando cria o arquivo (que ainda não existe) e já fecha

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


os.mknod('arquivo-teste4.txt')
os.mknod('/home/juclops/geek.txt')

# OBS: Se você estiver utilizando no MacOs, pode haver um erro de PermissionError
# OBS: Criando um arquivo via mknod() se oarquivo já existir teremos o erro FileExistsError


# Criando diretórios - únicos (um a um)

os.mkdir('templates')

# OBS: A função cria um diretório se este não existir, caso exista, teremos FileExistsError

os.mkdir('etc/templates')

# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError

# Criando multi-diretórios - árvore de diretórios
os.makedirs('geek/templates/university')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('geek/templates/university', exist_ok=True)
# OBS: Caso exista, com o argumento exist_ok=True, ignorará o erro


# Renomear arquivos e diretórios

# Diretórios
os.rename('geek', 'geek2')
# OBS: Se o diretório não existir, teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError


# Arquivos
os.rename('texto.txt', 'text.txt')


# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo
# ou diretório, eles não vão para a lixeira. Eles somem

os.remove('geek.txt')  # Feito para remover somente arquivos

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver
# em uso, você terá um erro

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo. Teremos um IsADirectoryError


# Removendo diretórios vazios

os.rmdir('templates')
# OBS: Se o diretório tiver qualquer conteúdo, teremos um OSError
# OBS: Se o diretório não existir, teremos um FileNotFoundError


# Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios
os.removedirs('geek2')
# OBS: Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.


# Importando a biblioteca send2trash
from send2trash import send2trash

os.remove('cesta1.txt')  # Não vai para a lixeira. É deletado imediatamente
send2trash('cesta2.txt')  # Vai para a lixeira. pode ser restaurado.

# OBS: Se o arquivo não existir, teremos OSError

send2trash('newdir')  # Removendo diretórios para a lixeira



# Trabalhando com arquivos e diretórios temporários

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei o diretório temporario em {tmp}")
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo  o mesmo e dentro
# dele criando um arquivo para escrevermos um texto. No final, usamos
# um input() só para mantermos os arquivos temporários 'vivos' dentro
# dos blocos with.

# OBS: Possivelmente o código acima não irá funcionar se você estiver
# utilizando windows. Por conta desse sistema trabalhar de forma diferente
# com arquivos temporários

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# Em arquivos temporários, só conseguimos escrever bits, por isso
# utilizamos b com uma string

# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""

import os
import tempfile


