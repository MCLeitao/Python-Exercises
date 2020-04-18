# Create a program that reads a real number from the keyboard and shows the entire portion on the screen

from math import trunc

n = float(input('Type a real number: '))
print('The entire part of {}{}{} is {}{}{}'.format('\033[1;32m', n, '\033[m', '\033[1;34m', trunc(n), '\033[m'))

# or
# n = float(input('Type a number: '))
# print('The entire part of {} is {}'.format(n, int(n)))
