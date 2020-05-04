# Improve the game in exercise ex028 where the computer will "think" of a number between 0 and 10.
# Only now the player will try to guess until he gets it right, showing in the end how many guesses it took to win.

from random import randint

"""
print('{:-^60}'.format(' I thought of a number (0 to 10), try to guess '))
computer = randint(0, 10)  # Makes the computer "think"
player = ''
hunches = 0
while player != computer:
    player = int(input('Enter your guess: '))
    hunches += 1
    if player < computer:
        print('\033[31mMore... Try again!!\033[m')
    elif player > computer:
        print('\033[31mLess... Try again!\033[m')
print(f'You are Right!! And it took {hunches} guesses to win.')
"""

# or:

print('{:-^60}'.format(' I thought of a number (0 to 10), try to guess '))
computer = randint(0, 10)  # Makes the computer "think"
hit = False
hunches = 0
while not hit:
    player = int(input('Enter your guess: '))
    hunches += 1
    if player == computer:
        hit = True
    else:
        if player < computer:
            print('\033[31mMore... Try again!!\033[m')
        else:
            print('\033[31mLess... Try again!!\033[m')
print(f'You are Right!! And it took {hunches} guesses to win.')
