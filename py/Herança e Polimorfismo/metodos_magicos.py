"""
POO - Métodos mágicos

Métodos mágicos são todos os métodos que utilizam dunder.

# dunder init -> método construtor __init__
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

Dunder > Double Underscore

# dunder repr -> representação do objeto
    def __repr__(self):
        return f'{self.titulo}, escrito por {self.autor}'

# dunder str -> representação em string
OBS: Sobresai ao metodo repr
    def __str__(self):
        return self.titulo

"""

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo}, escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'Objeto {self} deletado com sucesso')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for x in range(other):
                msg += str(self) + ' '
            return msg
        return 'Não posso multiplicar'

livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)
print(len(livro1))

print(livro1 + livro2)

print(livro1 * 3)