# Redo ex009, showing the multiplication table of a number that the user chooses, only now using a for loop.

num = int(input('Enter a integer o see your multiplication table: '))
mult = 0
print('-' * 12)
for cont in range(1, 11):
    mult = num * cont
    print(f'{num} x {cont:^2} = {mult}')
print('-' * 12)
