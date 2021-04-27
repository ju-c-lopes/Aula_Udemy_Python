"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    -> not
Operadores binários:
    -> and, or, is
"""

ativo = True
logado = False

if ativo and logado:
    print("Bem-vindo Usuário")
else:
    print("Você precisa ativar sua conta, cheque seu email")

if ativo or logado:
    print("Bem-vindo Usuário")
else:
    print("Você precisa ativar sua conta, cheque seu email")

if not logado:
    print("Você precisa ativar sua conta, cheque seu email")
else:
    print("Bem-vindo Usuário")
