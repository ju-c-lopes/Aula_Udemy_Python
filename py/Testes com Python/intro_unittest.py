"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste unitário é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser:
    - funções
    - métodos
    - classes
    - módulos
    - etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para a sua unidade

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Método                      Checa que
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x is True
assertFalse(x)              x is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a is in b
assertNotIn(a, b)           a is not in b
assertIsInstance(a, b)      a is instance of b
assertNotIsInstance(a, b)   a is not instance of b

Por convenção, todos os testes em um test case, devem ter
seu nome iniciado com test_

# Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no mode verbose

python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings nos nossos testes.
"""

# Prática - Utilizando a abordagem TDD

