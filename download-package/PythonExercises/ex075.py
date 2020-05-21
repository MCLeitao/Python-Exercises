# Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, show: A) How many
# times did the value 9 appear. B) In which position the first value 3 was entered. C) What were the even numbers.

numbers = (int(input('Enter a number: ')),
           int(input('Enter another number: ')),
           int(input('Enter one more number: ')),
           int(input('Enter the last number: ')))
print(f'You have entered the values: {numbers}')
print(f'The value 9 appeared {numbers.count(9)} times.')
if 3 in numbers:
    print(f'The value 3 appeared first in the {numbers.index(3) + 1}ª position.')
else:
    print('The value 3 was not entered in any position.')
print('The even values entered were:', end=' ')
for number in numbers:
    if number % 2 == 0:
        print(f'{number}', end=' ')
    else:
        print('-', end=' ')
