"""
Documentando funções com Docstrings

print(help(print))

OBS: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()
"""

# Exemplos


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'


print(help(diz_oi))

print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Pôtencia que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


help(exponencial)

print(exponencial.__doc__)
