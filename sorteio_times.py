import random
import numpy as np


def dividir_equipes():
    times = int(input('Digite a quantidade de times: '))
    path = 'palavras.txt'

    with open(path, 'r') as file:
        jogadores = file.readlines()

    random.shuffle(jogadores)
    splits = np.array_split(jogadores, times)

    print(splits)


dividir_equipes()
