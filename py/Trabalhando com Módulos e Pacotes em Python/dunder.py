"""
Dunder Name e Dunder Main

Dunder -> Double Under

Dunder Name -> __name__
Dunder Main -> __main__

Em Python, são utilizados dunde para criar funções, atributos, propriedades e
etc utilizando Double Under para não gerar conflito com os nomes desses
elementos na programação

# Na linguagem C, temos um programa da seguinte forma:

int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){
}

# Em Python, se executarmos um módulo Python diretamente na linha de comando,
internamente o Python atribuirá à variavvel __name__ o valor __main__,
indicando que este mósulo é o módulo de execução principal.

Main -> Significa principal.

Caso o arquivo seja executado via importação __name__ será o nome do arquivo

from funcoes_com_parametro import soma_impares

print(soma_impares([1, 3, 4, 7]))
"""

import primeiro
import segundo
