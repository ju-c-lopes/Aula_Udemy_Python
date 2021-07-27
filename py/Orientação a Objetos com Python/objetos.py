"""
POO - Objetos

Objetos são instâncias da classe. Ou seja, após o mapeamento do objeto do
mundo real para sua representação computacional, devemos poder criar quantos
objetos forem necessários. Podemos pensar nos objetos/instâncias de uma classe
como variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        estado = 'ligada' if self.__ligada else 'desligada'
        print(estado)

    def ligar_desligar(self):
        self.__ligada = not self.__ligada
        return self.__ligada


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias ou Objetos
lamp1 = Lampada('branca', 110, 60)
cc1 = ContaCorrente(5000, 20000)
user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
