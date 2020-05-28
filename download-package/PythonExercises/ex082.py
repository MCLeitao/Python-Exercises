# Create a program that will read multiple numbers and put them in a list.
# After that, create two extra lists that will contain only the even values and the odd values entered, respectively.
# At the end, show the content of the three lists generated.

numbers = list()
even = list()
odd = list()
while True:
    number = int(input('Enter a value: '))
    numbers.append(number)
    choice = ' '
    while choice not in 'YN':
        choice = str(input('Do you want continue? [Y/N] ')).strip().upper()[0]
    if choice == 'N':
        break
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print('-=' * 15)
print(f'The complete list is {numbers}')
print(f'The even number list is {even}')
print(f'The odd number list is {odd}')
