"""
Any e All

# função booleana
all() -> Retorna True se todos os elementos do iterável são verdadeiros ou se o
iterável está vazio.


# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros?
# Resultado é False, pois o 0 é o valor booleano False
# Se retiramos o 0 obteremos como resultado True
# Se o iterável estiver vazio, obteremos True
print(all([]))
print(all('Geek'))  # Uma string é um iterável, então  obteremos True
print(all(''))  # True
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']  #, 'Daniel'] -> com Daniel será False
print(all([nome[0] == 'C' for nome in nomes]))

# OBS: um iterável vazio convertido em boolean é False, mas
# o all entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))
# verificando se cada letra está presente aqui

print(all([num for num in [4, 6, 2, 10, 8] if num % 2 == 1]))

"""

# =================================================================================


"""
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

"""

print(any([0, 1, 3, 4]))  # True
print(any([0, False, {}, []]))  # False
print(any([0, False, {}, [], 1]))  # True

nomes = ['Carlos', 'Camila', 'Cristina', 'Cassiano', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
# Com o any obtemos True, se fosse all, obteriamos False

print(any([num for num in [4, 6, 2, 10, 8, 9] if num % 2 == 0]))
