# Create a program where the user can enter five numeric values and register them in a list, already in the correct
# insertion position (without using the sort ()). At the end, show the ordered list on the screen.

values = list()
for cont in range(0, 5):
    number = int(input('Enter a value: '))
    if cont == 0 or number > values[-1]:
        values.append(number)
        print('Added at the end of the list...')
    else:
        position = 0
        while position < len(values):
            if number <= values[position]:
                values.insert(position, number)
                print(f'Added in position {position} of the list...')
                break
            position += 1
print('-=' * 15)
print(f'The values entered in order were {values}')
