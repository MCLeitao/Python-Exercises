# Make a program that reads an integer and says whether or not it is a prime number.

n = int(input('Enter a Integer: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mThe number {} was divisible {} times'.format(n, tot))
if tot == 2:
    print('And so It is a PRIMER NUMBER!'.format(n))
else:
    print('And so It is NOT a primer number')
