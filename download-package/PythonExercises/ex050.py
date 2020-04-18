# Develop a program that reads 6 integers and shows the sum of only those that are even.
# If the value entered is odd, disregard it.

s = 0
for c in range(0, 7):
    n = int(input('Enter a Number: '))
    if n % 2 == 0:
        s += n
print('The Sum of the Even Numbers is: {}'.format(s))
