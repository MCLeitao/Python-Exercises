# Create a program where the user can enter several numeric values and register them in a list. If the number already
# exists inside, it will not be added. At the end, all the unique values entered will be displayed, in ascending order.

values = list()
while True:
    number = (int(input('Enter a value: ')))
    if number not in values:
        values.append(number)
        print('Added value successfully...')
    else:
        print('Value already exists. Not added...')
    choice = ' '
    while choice not in 'YN':
        choice = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if choice == 'N':
        break
print('-=' * 30)
values.sort()
print(f'You entered the values {values}')
