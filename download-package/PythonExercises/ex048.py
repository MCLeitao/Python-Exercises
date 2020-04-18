# Make a program that calculates the sum between all the odd numbers that are multiples of three
# and that are in the range of 1 to 500.

s = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print('The SUM is: {}'.format(s))
