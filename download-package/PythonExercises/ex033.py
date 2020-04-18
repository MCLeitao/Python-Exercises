# Make a program that reads three numbers and shows which is the largest and which is the smallest

n1 = int(input('Type a number: '))
n2 = int(input('Type another number: '))
n3 = int(input('Type another one: '))
# Checking who is the smallest
smallest = n1
if n2 < n1 and n2 < n3:
    smallest = n2
if n3 < n1 and n3 < n2:
    smallest = n3
# Checking who is the largest
largest = n1
if n2 > n1 and n2 > n3:
    largest = n2
if n3 > n1 and n3 > n2:
    largest = n3
print('The smallest value entered was {}'.format(smallest))
print('The largest value entered was {}'.format(largest))
