"""
Lendo arquivos CSV

CSV - Comma separated Values - Valores Separados por Vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6

'geek', 'university', 'python'

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6

'geek'; 'university'; 'python'

# Separador por espaço
1 2 3 4 5 6

'geek' 'university' 'python'

OBS: Podemos usar muitos outros (praticamente qualquer) caracteres como separador,
devemos apenas ter um padrão, usando o mesmo por todo arquivo

http://dados.gov.br/dataset

# Possível de se trabalhar, porém não é ideal
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(type(dados))  # retorna tipi str
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)  # método reader retorna um iterator que podemos usar...
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')


from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

"""

# Com outro separador
# OBS: por padrão é virgula, caso fosse ';' informaríamos isso no delimiter

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
