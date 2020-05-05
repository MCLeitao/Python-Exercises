# Create a program that reads several integers from the keyboard.
# The program will only stop when the user enters the value 999, which is the stop condition.
# At the end, show how many numbers were entered and what was the sum between them (disregarding the flag).

"""
num = int(input('Enter a integer [999 to stop]: '))
cont = sum = 0
while num != 999:
    sum += num
    cont += 1
    num = int(input('Enter a integer [999 to stop]: '))
print('Tou typed {} numbers and the sum between them is {}'.format(cont, sum))
"""

# Or:

num = cont = sum = 0
while num != 999:
    num = int(input('Enter a integer [999 to stop]: '))
    if num != 999:
        sum += num
        cont += 1
print(f'You typed {cont} numbers and the sum between them is {sum}.')
