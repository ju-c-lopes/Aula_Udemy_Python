"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importa e fazer uso do módulo os.

os -> Operating System - Sistema Operacional


# Fazer o import
import os
# getcwd() -> Pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd())  # /../py

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/juclops/'))  # true


# OBS: Usuários windows
# Se você estiver utilizando um computador com windows
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\juclops'))



# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)


# Podemos ter mais detalhes no sistema operacional
print(os.uname())


import sys
print(sys.platform)


import os
print(os.getcwd())
os.mkdir('newdir')

res = os.path.join(os.getcwd(), 'newdir')

os.chdir(res)
print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório
# atual e o segundo o diretório que será juntado ao atual.


# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())
print(len(os.listdir()))
print(os.listdir('/home'))
print(len(os.listdir('/home')))

"""

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

# print(list(os.scandir()))
scanner = os.scandir()

arquivos = list(scanner)

# print(dir(arquivos[0]))

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # é um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatísticas sobre o arquivo

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo

scanner.close()
