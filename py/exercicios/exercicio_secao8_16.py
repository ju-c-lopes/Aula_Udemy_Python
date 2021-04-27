"""

Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando
vários simbolos de igual (Ex: ===============). A função recebe por parâmetro quantos sinais
de igual serão mostrados.

"""


def desenhar_linha(n):
    """
    Desenhará uma linha com a quantidade de sinais de igual informada no parâmetro n
    """
    print('\n')
    i = 0
    while i < n:
        print('=', end='')
        i += 1
    print('\n')
    

desenhar_linha(100)
