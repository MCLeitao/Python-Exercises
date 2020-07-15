# Create a program where 4 players roll a die and have random results. Store these results in a dictionary.
# In the end, put this dictionary in order, knowing that the winner has the highest number in the die.

from random import randint
from time import sleep
from operator import itemgetter

players = dict()
ranking = dict()  # or list()
'''
players = {'player1': randint(1, 6),
           'player2': randint(1, 6),
           'player3': randint(1, 6),
           'player4': randint(1, 6)}
'''
# or
for cont in range(0, 4):
    players[f'player{cont + 1}'] = randint(1, 6)

print('Drawn values:')
for key, value in players.items():
    print(f'{key} rolled {value} on the die.')
    sleep(1)
print('--' * 15)

# Dictionaries do not sort in the original, you need to create another dictionary
print('Player ranking:')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
# print(ranking) → Note that this dictionary is treated as a list
for index, value in enumerate(ranking):
    print(f'{index + 1}º place: {value[0]} with {value[1]}.')
    sleep(1)
