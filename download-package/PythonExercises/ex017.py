# Make a program that reads the length of the opposite side and the adjacent side of a right angled triangle
# calculate and show the length of the hypotenuse

from math import hypot

o = float(input('Enter the length of the opposite side: '))
a = float(input('Enter the length of the adjacent side: '))
# h = (o ** 2 + a ** 2) ** (1/2)
print('The length of hypotenuse is {}{:.2f}{}'.format('\033[1;31;40m', hypot(o, a), '\033[m'))
# print('The length of hypotenuse is {:.2f}'.format(h))
