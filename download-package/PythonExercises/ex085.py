# Create a program where the user can enter seven numerical values and register them in a single list that keeps the
# odd and even values separate. At the end, show even and odd values in ascending order.

numbers = [[], []]
value = 0
for cont in range(0, 7):
    value = int(input(f'Enter the {cont + 1}ª value: '))
    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)
numbers[0].sort()
numbers[1].sort()

print('-=' * 30)
print(f'The even values entered were: {numbers[0]}.')
print(f'The odd  values entered were: {numbers[1]}.')
