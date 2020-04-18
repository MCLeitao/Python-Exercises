# Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try to find out
# which number was chosen by the computer. The program should write on the screen if the user won or lost.

from random import randint
from time import sleep
import emoji

r = randint(0, 5)  # Makes the computer "think"
print('-=-' * 20)
print('I`ll think of a number between 0 and 5. Try to guess ...')
print('-=-' * 20)
u = int(input('what number did i think of? '))  # User try to find out
print('PROCESSING ...')
sleep(3)
if u == r:
    print('Congratulations!! You got it right!!')
else:
    print('I WON!!. I thought of number {} {} {} and not {}!'.format('\033[1;30;41m', r, '\033[m', u))
print(emoji.emojize("Try again :wink: !!", use_aliases=True))
