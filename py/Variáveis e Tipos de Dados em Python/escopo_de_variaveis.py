"""
Escopo de Variáveis

Escopo -> Limitação

Dois casos de escopo:

1 -> variáveis globais;
    - variáveis globais são reconhecidas, ou seja,  seu escopo compreente todo o programa.

2 -> variáveis locais;
    - variáveis locais são reconhecidas apenas nos blocos onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada

Para  declarar variável em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor á mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

No Python é possivel fazer a re-atribuição, inserir dados de outro tipo a mesma variável,
o que não é possivel em C ou em Java;
"""

numero = 23  # Exemplo de variável global, em qualquer parte do programa tenho acesso a ela
print(type(numero))

numero = 'Oi'
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10  # A variável novo está declarada dentro do bloco do if. Portanto é local
    print(novo)
