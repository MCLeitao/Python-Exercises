# Redo ex009, showing the multiplication table of a number that the user chooses, only now using a for loop.

num = int(input('Enter a integer o see your multiplication table: '))
print('-' * 12)
for c in range(1, 11):
    print('{} x {:2}  = {}'.format(num, c, num * c))
print('-' * 12)
