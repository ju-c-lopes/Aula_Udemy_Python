import random

# https://www.alt-codes.net/suit-cards.php

NAIPES: list = '♠ ♡ ♢ ♣'.split()
CARTAS: list = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio: bool = False) -> list:
    """Cria um baralho com 52 cartas"""
    baralho: list = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: list) -> tuple:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]

def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas: list = criar_baralho(aleatorio=True)
    jogadores: list = 'P1 P2 P3 P4'.split()
    maos: dict = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()