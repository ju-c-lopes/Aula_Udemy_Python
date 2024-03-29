"""
Escrevendo um iterador customizado

para criar um iterador, devem ser usadas as funções __iter__ e __next__ sobrecarregadas
"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 5)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))


for n in Contador(1, 11):
    print(n)
