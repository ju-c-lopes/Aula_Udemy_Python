"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. é uma palavra reservada, assim como def ou qualquer outra em Python

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções
e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro("Mensagem de erro")
# Exemplo
raise ValueError('Valor Incorreto')

# Exemplo Real
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore(True, "preto")

# Exemplo refatorado
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'vermelho', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A Cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore("Geek", "branco")

OBS: O raise, assim como o return, finaliza a função.
Ou seja, nada após o raise é executado
"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'vermelho', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A Cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore("Geek", "branco")
