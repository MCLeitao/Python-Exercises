# Make a program that shows the multiplication table of several numbers, one at a time, for each value entered by the
# user. The program will be interrupted when the requested number is negative.

# cont = 1
print('--' * 15)
while True:
    num = int(input('Multiplication table of what value? '))
    print('--' * 15)
    if num < 0:
        break
    for cont in range(1, 11):  # while cont <= 10:
        print(f'{num} x {cont:^2} = {num * cont}')
        # cont += 1
    # cont = 1
    print('--' * 15)
print('Multiplication table program ended. Check back often!')
