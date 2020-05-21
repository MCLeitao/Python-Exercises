# Create a program that will generate five random numbers and place it in a tuple.
# After that, show the list of generated numbers and also indicate the lowest and highest values that are in the tuple.

from random import randint

numbers = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print('The values drawn were:', end=' ')
for number in numbers:
    print(f'{number}', end=' ')
print(f'\nThe highest amount drawn was {max(numbers)}.')
print(f'The lowest amount drawn was {min(numbers)}.')
