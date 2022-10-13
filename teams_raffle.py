import random                                                       #here I import the random library
import numpy as np                                                  #here I import the numpy library


def divide_teams():                                                 #declare a function
    teams = int(input('input the number of teams: '))               #add a variable to it with an input as its value
    path = 'words.txt'                                              #another variable and its fixed value as a .txt file

    with open(path, 'r') as file:                                   #the .txt file is opened to be read
        players = file.readlines()                                  #the variable players receives the path content as its value

    random.shuffle(players)                                         #the content of the players variable is shuffled
    splits = np.array_split(players, teams)                         #the content of the players variable is divided by the number of players and teams

    print(splits)                                                   #the raffle is displayed for the user.


divide_teams()                                                      #it calls the function
