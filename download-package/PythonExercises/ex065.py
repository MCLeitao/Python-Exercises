# Create a program that reads several integers from the keyboard.
# At the end of the run, show the average of all values and which was the highest and lowest values read.
# The program should ask the user whether or not he wants to continue to enter the values.

num = 0
answer = 'Y'
sum = cont = average = 0
highest = lowest = 0
while answer in 'Yy':
    num = int(input('Enter a integer: '))
    cont += 1
    sum += num
    if cont == 1:
        highest = num
        lowest = num
    else:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
    answer = str(input('Want to continue? [Y/N] ')).strip().upper()[0]
average = sum / cont
print(f'You typed {cont} numbers and the average is {average} \nThe highest was {highest} and lowest was {lowest}.')
