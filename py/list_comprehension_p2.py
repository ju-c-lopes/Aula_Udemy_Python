"""

List Comprehension

Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehension

"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 ==0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# Qualquer numero par módulo de 2 é 0, e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
# para cada numero in numeros, salva numero se not numero módulo 2. Lembrando que retorna não False

impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)