# Develop a program that reads the length of three lines and tells the user whether or not they can form a triangle.

print('-=-' * 10)
print('Triangle Analyzer')
print('-=-' * 10)

a = float(input('Type the first segment: '))
b = float(input('Type the second segment: '))
c = float(input('Type the third segment: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('The above segments CAN form a triangle')
else:
    print('The above segment CAN NOT form a triangle')
