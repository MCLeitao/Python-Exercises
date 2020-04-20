# Make a program that reads an integer and says whether or not it is a prime number.

num = int(input('Enter a Integer: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mThe number {} was divisible {} times'.format(num, tot))
if tot == 2:
    print('And so It is a PRIMER NUMBER!')
else:
    print('And so It is NOT a primer number')
