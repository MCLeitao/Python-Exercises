# Create a program that has a tuple fully populated with a count in full, from zero to twenty.
# Your program should read a number on the keyboard (between 0 and 20) and show it in full.


full = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    number = int(input('Enter a number between 0 and 20: '))
    if 0 <= number <= 20:
        print(f'You typed the number \033[1:32m{full[number]}\033[m.')
        choice = ' '
        while choice not in 'YN':
            choice = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
        if choice in 'N':
            break
    else:
        print('Try again.', end=' ')
print('END')
