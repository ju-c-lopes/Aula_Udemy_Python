"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções.
- Decorators envolvem outras funções e aprimoram seus comportamentos.
- Decorators também são exemplos de Higher Order Functions.
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

|-----------------------------------------|
|        Function Decorator               |
-------------------------------------------

-------------------------------------------------
|  |-----------------------------------------|  |
|  |          Função Decorada                |  |
|  |-----------------------------------------|  |
|-----------------------------------------------|

# Decorators como funções (Sintaxe não remomendada / Sem Açúcar Sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Testando 1


teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print("TE ODEIO")


raiva_educada = seja_educado(raiva)

raiva_educada()



# Decorators com Syntax Sugar (Açucar Sintático)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando


apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()
"""
"""
|--------------------------------------------------------
|   HOME   |   SERVIÇOS    |    PRODUTOS    |  ADMIN    |
---------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/admn

# OBS: Não é código funcional, é apenas exemplo

def checa_login(request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')

def home(request):
    return "Pode acessar home"

def servicos(request):
    return "Pode acessar serviços"

def produtos(request):
    return "Pode acessar produtos"

@checa_login
def admin(request):
    return "Pode acessar admin"

"""

# OBS: Não confunda Decorator com decorator function
# Decorator é @
# Decorator function é a função
