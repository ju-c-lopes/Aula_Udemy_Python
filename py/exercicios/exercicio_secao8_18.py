"""

Faça uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o
resultado de x^z para o programa principal. Atenção não utilize nenhuma função pronta
de exponenciação.

"""


def potencia(x, z):
    """
    Calculará a potênciação tendo o primeiro número como base e o segundo como expoente.
    """
    pot = x ** z
    return pot


print(potencia(3, 5))
