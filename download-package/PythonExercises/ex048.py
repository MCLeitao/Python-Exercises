# Make a program that calculates the sum between all the odd numbers that are multiples of three
# and that are in the range of 1 to 500.

sum = 0  # Accumulator
cont = 0  # Counter
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont += 1  # cont = cont + 1
        sum += num  # sum = sum + c
print(f'The SUM of all {cont} request values is {sum}')
# Another way:
# Perform more iterations - use more processor capacity
"""
for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        cont += 1
        sum += num
print(f'The SUM of all {cont} request values is {sum}')
"""
