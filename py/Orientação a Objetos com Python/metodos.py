"""
POO - Métodos

- Métodos (funções) ->  Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos:
    - Métodos de Instância
    - Métodos de Classe

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e sua
função é construir o objeto a partir da classe.

OBS: Toto elemento em Python que inicia e finaliza com duplo underline é chamado
de dunder (double underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO: Por nmais que possamos criar nossas própruas funções utilizando dunder
(underline no inicio e no fim), não é aconselhado. Python possui vários métodos
com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas
funções mágicas internas da linguagem. Então, evite ao máximo. De preferência
nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome
terá as palavras separadas por underline _

p1 = Produto('PlayStation 4', 'Vídeo Game', 2300)
print(p1.desconto(20))

# print(Produto.desconto(p1, 40))  # p1 é o self

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuario criado com sucesso!')
else:
    print('Senha não confere...')
    user = None
    exit(1)

senha = input('Informe a senha para acesso: ')

if user:
    if user.checa_senha(senha):
        print('Acesso concedido.')
    else:
        print('Acesso Negado')
        exit(1)
else:
    exit(1)

if user:
    senha = input(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso errado


# Métodos de Classe em Python são conhecidos como métodos estáticos em outras linguagens


# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto."""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(cls)
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, psw):
        if cryp.verify(psw, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método estático

print(Usuario.contador)
print(Usuario.definicao())
