"""

Set Comprehension

Lista = [1, 2, 3,4 , 5]
Set = {1, 2, 3, 4, 5}  # Não aceita valores repetidos, não guardam ordenação

"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 for x in range(10)}
# Desafio - numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# DESAFIO: Faça uma alteração na estrutura acima para gerar um dicionário, ao invés de set

# Pra finalizar

letras = {letra for letra in 'Geek University'}
print(letras)
