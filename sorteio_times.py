import random
import numpy as np


def divide_teams():
    teams = int(input('input the number of teams: '))
    path = 'words.txt'

    with open(path, 'r') as file:
        players = file.readlines()

    random.shuffle(players)
    splits = np.array_split(players, teams)

    print(splits)


divide_teams()
