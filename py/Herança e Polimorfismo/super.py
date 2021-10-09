"""
POO - O método super()

O método super() se refere à super classe

"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # sintaxe possivel para usar porém,
        super().__init__(nome, especie)         # este é o recomendado
        super().faz_som('auauaua')  # exemplo mostrando acesso a qualquer metodo do pai
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')