# Make a program that reads an integer and says whether or not it is a prime number.

num = int(input('Enter a number: '))
tot = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{cont}', end=' ')
print(f'\n\033[mThe number {num} was divisible {tot} times.')
if tot == 2:
    print('And so It is a PRIMER NUMBER!')
else:
    print(f'And so It is NOT a primer number!')
