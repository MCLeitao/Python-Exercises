# Create a program that reads two values and shows a menu on the screen: [1] ADD; [2] MULTIPLY; [3] BIGGER; [4] NEW
# NUMBERS; [5] EXIT PROGRAM. Your program must perform the requested operation in each case

from time import sleep

n1 = float(input('First value: '))
n2 = float(input('Second value: '))
mult = sum = higher = 0
option = 0
while option != 5:
    print('OPERATIONS: \n[1] ADD \n[2] MULTIPLY \n[3] HIGHEST \n[4] NEW NUMBERS  \n[5] EXIT PROGRAM')
    option = int(input('> Your choice: '))
    if option == 1:
        sum = n1 + n2
        print(f'The sum between {n1} + {n2} is {sum}.')
    elif option == 2:
        mult = n1 * n2
        print(f'The multiplication between {n1} x {n2} is {mult}.')
    elif option == 3:
        if n1 > n2:
            higher = n1
            print(f'Between {n1} and {n2} the highest value is {higher}.')
        elif n1 < n2:
            higher = n2
            print(f'Between {n1} and {n2} the highest value is {higher}.')
        else:
            print('The values are equal.')
    elif option == 4:
        print('Enter the numbers again.')
        n1 = int(input('First value: '))
        n2 = int(input('First value: '))
    elif option == 5:
        print('Finishing...')
    else:
        print('\033[31mINVALID CHOICE\033[m')
    print('-' * 15)
    sleep(2)
print('\033[32mEND PROGRAM\033[m')
