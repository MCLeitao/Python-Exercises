# Create a program that makes the computer play Jokenpo with you.

from random import choice
# from random import randint
from time import sleep

print('{:=^40}'.format(' Let`s play JOKENPO!! '))
player = str(input('Make your choice: ')).strip().upper()
comp = choice(['ROCK', 'PAPER', 'SCISSORS'])
# items = ('ROCK', 'PAPER', 'SCISSORS')
# comp = randint(0, 2)
# print('The computer chose {}'.format(items[comp]))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print('My  choice  is: {}'.format(comp))
print('Your choice is: {}'.format(player))
print('-=' * 10)
if comp == 'ROCK':
    if player == 'ROCK':
        print('We TIED!!')
    elif player == 'PAPER':
        print('You win!!')
    elif player == 'SCISSORS':
        print('I won!!')
    else:
        print('INVALID PLAY')
elif comp == 'PAPER':
    if player == 'ROCK':
        print('I won !!')
    elif player == 'PAPER':
        print('We TIED!!')
    elif player == 'SCISSORS':
        print('You win!!')
    else:
        print('INVALID PLAY')
elif comp == 'SCISSORS':
    if player == 'ROCK':
        print('You win!!')
    elif player == 'PAPER':
        print('I won!!')
    elif player == 'SCISSORS':
        print('We TIED!!')
    else:
        print('INVALID PLAY')

# if player == comp:
#     print('We Tied !!')
# elif player == 'ROCK' and comp == 'PAPER':
#     print('I won !!')
# elif player == 'PAPER' and comp == 'ROCK':
#     print('You win !!')
# elif player == 'ROCK' and comp == 'SCISSORS':
#     print('You won !!')
# elif player == 'SCISSORS' and comp == 'ROCK':
#     print('I won !!')
# elif player == 'ROCK' and comp == 'SCISSORS':
#     print('You won !!')
# elif player == 'PAPER' and comp == 'SCISSORS':
#     print('I win !!')
# else:
#    print('You won !!')
