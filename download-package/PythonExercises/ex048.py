# Make a program that calculates the sum between all the odd numbers that are multiples of three
# and that are in the range of 1 to 500.

sum = 0  # Accumulator
cont = 0  # Counter
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1  # cont = cont + 1
        sum += c  # sum = sum + c
print('The SUM of all {} request values is {}'.format(cont, sum))
