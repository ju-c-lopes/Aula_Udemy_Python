"""
PEP 484
"""

# Type Hinting

# def cumprimentar(nome: str) -> str:
#     return f'Olá, {nome}'
#
# print(cumprimentar('Geek'))

def cabecalho(texto: str, alinhamento: bool=True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('geek'))

print(cabecalho('geek', alinhamento=False))

print(cabecalho('geek university', 'geek'))  # rodará por string não vazia ser convertida para True

print(cabecalho('University', 0))  # rodará por int 0 ser convertido para False