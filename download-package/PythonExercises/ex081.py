# Create a program that will read several numbers and put them on a list. After that, show: A) How many numbers were
# entered. B)The list of values, ordered descending. C)Whether value 5 was entered and whether or not it is in the list.

numbers = []
while True:
    numbers.append(int(input('Enter a value: ')))
    choice = ' '
    while choice not in 'YyNn':
        choice = str(input('Do you want to continue? [Y/N] ')).strip()[0]
    if choice in 'Nn':
        break
print('-=' * 15)
print(f'You typed {len(numbers)} numbers.')
numbers.sort(reverse=True)
print(f'The values in descending order are {numbers}')
if 5 in numbers:
    print('The value 5 is part of the list in the positions', end=' ')
    for key, value in enumerate(numbers):
        if value == 5:
            print(f'{key + 1}... ', end='')
else:
    print('The value 5 was not found in the list!')
