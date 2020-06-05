# Make a program that helps a PowerBall player to make guesses. The program will ask how many games will be generated
# and will raffle 6 numbers between 1 and 60 for each game, registering everything in a composite list.

from random import randint
from time import sleep

print('-' * 35)
print(f'{"PLAY ON POWERBALL":^35}')
print('-' * 35)

amount = int(input('How many games do you want me to draw? '))
game = list()
guesses = list()
print(f'{" SORTING THE GAMES ":-^35}')
for cont in range(0, amount):
    unity = 0
    while True:
        number = randint(1, 60)
        if number not in game:
            game.append(number)
            unity += 1
        if unity == 6:
            break
    game.sort()
    guesses.append(game[:])
    game.clear()
for index, game in enumerate(guesses):
    print(f'Game {index + 1}: {game}')
    sleep(1)
print(f'{" < GOOD LUCK! > ":-^35}')
