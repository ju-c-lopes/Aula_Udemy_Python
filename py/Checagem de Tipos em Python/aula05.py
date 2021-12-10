def cabecalho(texto: str, alinhamento: bool=True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('geek'))

print(cabecalho('geek', alinhamento=False))

print(cabecalho('geek university', 'geek'))  # rodará por string não vazia ser convertida para True

print(cabecalho('University', 0))  # rodará por int 0 ser convertido para False

# A biblioteca mypy verifica tipo de dado conforme específicado, apontando erros
# onde forem diferentes, como tipo bool acima, sendo passado uma string

# Porém, funciona com este tipo de abordagem, funções comuns, sem explicitar tipo não funciona