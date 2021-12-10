import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

# print(circunferencia(8))

def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

# cabecalho(texto=42, alinhamento='geek')

def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto='42', alinhamento=False)
