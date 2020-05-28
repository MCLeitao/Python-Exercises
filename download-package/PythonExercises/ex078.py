# Make a program that reads 5 numeric values and saves them in a list.
# At the end, show which was the highest and lowest value entered and their respective positions in the list.

values = list()
# max = min = 0
for cont in range(0, 5):
    values.append(int(input(f'Enter a value for position {cont}: ')))
''' if cont == 0:
        max = min = values[cont]
    else:
        if values[cont] > max:
            max = values[cont]
        if values[cont] < min:
            min = values[cont] '''
print('=-' * 30)
print(f'You typed the values {values}')
highest = max(values)
print(f'The highest value entered was {highest} in positions', end=' ')
for key, value in enumerate(values):
    if value == highest:
        print(f'{key}...', end=' ')
lowest = min(values)
print(f'\nThe lowest  value entered was {lowest} in positions', end=' ')
for key, value in enumerate(values):
    if value == lowest:
        print(f'{key}...', end=' ')
