# Redo ex009, showing the multiplication table of a number that the user chooses, only now using a for loop.

n = int(input('Enter a integer o see your multiplication table: '))
print('-' * 12)
for c in range(0, 11):
    if c <= 9:
        print('{} x {}  = {}'.format(n, c, n * c))
    else:
        print('{} x {} = {}'.format(n, c, n * c))
print('-' * 12)
