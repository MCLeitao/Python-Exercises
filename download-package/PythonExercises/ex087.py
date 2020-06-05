# Improve the previous exercise, showing at the end: A) The sum of all typed even values.
# B) The sum of the values in the  third column. C) The highest value of the second line.

array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_even = sum_column = highest = 0
for row in range(0, 3):
    for column in range(0, 3):
        array[row][column] = int(input(f'Enter a value for [{row}, {column}]: '))
print('-=' * 25)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{array[row][column]:^5}]', end='')
        if array[row][column] % 2 == 0:
            sum_even += array[row][column]
    print()
print('-=' * 25)
print(f'The sum of the even values is {sum_even}.')
for row in range(0, 3):
    sum_column += array[row][2]
print(f'The sum of the values in the third column is {sum_column}.')
for column in range(0, 3):
    if column == 0 or array[1][column] > highest:
        highest = array[1][column]
print(f'The highest value in the second line is {highest}.')
