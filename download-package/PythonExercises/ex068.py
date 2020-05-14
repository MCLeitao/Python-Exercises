# Make a program that plays Odds or Evens with the computer. The game will only be stopped when the player loses,
# showing the total number of consecutive victories he has won at the end of the game.

from random import randint

print('=-' * 12)
print('LET`S PLAY ODDS OR EVENS')
print('=-' * 12)
vic = 0
while True:
    choice = str(input('Odd or Even? [O/E] ')).strip().upper()[0]
    while choice not in 'OE':
        print('\033[1:33mINVALID CHOICE\033[m')
        choice = str(input('Odd or Even? [O/E] ')).strip().upper()[0]
    player = int(input('Say a value: [0-10] '))
    while player < 0 or player > 10:
        print('\033[1:33mINVALID CHOICE\033[m')
        player = int(input('Say a value: [0-10] '))
    computer = randint(0, 10)
    total = player + computer
    print('--' * 12)
    print(f'You played {player} and the computer {computer}. Total {total} is', end=' ')
    print('EVEN' if total % 2 == 0 else 'ODD')
    print('--' * 12)
    if choice == 'E':
        if total % 2 == 0:
            print('You WON!')
            vic += 1
        else:
            print('You LOST!')
            print('=-' * 12)
            break
    elif choice == 'O':
        if total % 2 == 1:
            print('You WON!')
            vic += 1
        else:
            print('You LOST!')
            print('=-' * 12)
            break
    print('Let`s play again...')
    print('=-' * 12)
print(f'\033[1:31mGAMER OVER!\033[m \nYou won {vic} times.')
