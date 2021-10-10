"""
POO - Herança Múltipla

Herança múltipla nada mais é do que a possibilidade uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas

# OBS: A herança multipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;


# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3(Base1, Base2):
    pass

class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

# OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança
herdará todos os atributos e métodos das super classes.
"""

# EXEMPLO REAL

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} do mar!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


# TESTANDO...

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Eu sou Tux da terra! ???? Method Resolution Order - MRO
                            # Se inverter a super na classe, mudará o print

# Objeto é instância de...

print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de object? {isinstance(tux, object)}')