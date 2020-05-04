# Make a program that reads any number and shows its factorial.
# Ex. 5! = 5 x 4 x 3 x 2 x 1 = 120

# Using math package:

"""
from math import factorial
n = int(input('Enter a value: '))
f = factorial(n)
print(f'The factorial of {n} is {f}.')
"""

# Or using for loop:

"""
num = int(input('Enter a value: '))
factorial = 1
print(f'Calculating: {format}! = ', end='')
for cont in range(num, 0, -1):
    factorial *= cont
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    # print(f'{cont}', end= ' x ' if cont > 1 else ' = ')
print(f'{factorial}.')
"""

# Or using while loop:

num = int(input('Enter a value: '))
cont = num
factorial = 1  # Null factor of multiply is 1
print(f'Calculating: {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    # print(f'{cont}', end= ' x ' if cont > 1 else ' = ')
    factorial *= cont
    cont -= 1
print(f'{factorial}')
