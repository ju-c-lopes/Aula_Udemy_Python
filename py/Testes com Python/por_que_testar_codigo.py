"""
Porque testar nosso código?

Testes Automatizados!

            Aplicação Web
-------------------------------------
|                                   |
|        front-end e backend        |
-------------------------------------
|       testes automatizados        |
-------------------------------------

Porque testar nosso código?
    - Reduzir bugs (problemas) no código existente;
    - Garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Garantem que a refatoração que costumamos fazer não tragam novos bugs;

TDD- Test driven development (Desenvolvimento guiado por testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então voce escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase sempre um mantra que os desenvolvedore seguem,
conhecidos como:
    - Red;
    - Green;
    - Refactor;

"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.nome} está miando...')


felix = Gato('Felix')

felix.miar()

print(felix.nome)