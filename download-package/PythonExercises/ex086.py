# Create a program that creates a 3x3 dimension matrix and fills in values read from the keyboard.
# At the end, show the matrix on the screen, with the correct formatting.

"""
values = list()
row = column = 0
for cont in range(0, 9):
    number = int(input(f'Enter a value for [{row}, {column}]: '))
    values.append(number)
    column += 1
    if column == 3:
        row = 1
        column = 0
    if cont >= 5:
        row = 2
print('-=' * 15)
for cont in range(0, 9):
    print(f'[ {values[cont]:^4} ]', end=' ')
    if cont == 2 or cont == 5:
        print('')
"""
# Or
array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for column in range(0, 3):
        array[row][column] = int(input(f'Enter a value for [{row}, {column}]: '))
print('-=' * 15)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{array[row][column]:^5}]', end='')
    print('')
