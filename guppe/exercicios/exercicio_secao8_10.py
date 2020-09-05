"""
Exercicios Python - Seção 8

10. Faça uma função que receba dois números e retome qual deles é o maior.
"""

print('\nMostraremos qual entre dois números é o maior')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))


def mostrar_maior(x, y):
    """Analisará qual entre dois números informados é o maior"""
    if x > y:
        return f'Número {x} é o maior'
    elif x == y:
        return 'Ambos os números são iguais'
    return f'Número {y} é o maior'


print(mostrar_maior(num1, num2))
