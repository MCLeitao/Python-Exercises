# Develop a program that reads the first term and the reason for an arithmetic progression.
# At the end, show the first 10 terms of this progression.

print('-' * 22)
print('Arithmetic Progression')
print('-' * 22)
n = int(input('Enter a Number: '))
p = int(input('Enter the Reason: '))
s = 0
for c in range(0, 10):
    s = n + (p * c)
    print(s)
print('END')
