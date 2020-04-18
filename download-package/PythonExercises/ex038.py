# Write a program that reads two integer and compares them, showing a message on the screen.
#  The first value is greater; The second value is greater; There is no greater value, the two are equal.

n1 = int(input('First Value: '))
n2 = int(input('Second Value: '))
if n1 > n2:
    print('The FIRST value is GREATER')
elif n1 < n2:
    print('The SECOND value is GREATER')
else:
    print('The two values are EQUAL')
