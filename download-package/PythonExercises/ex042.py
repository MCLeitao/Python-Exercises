# Develop a program that reads the length of three sides and tells the user whether or not they can form a triangle.
# And if they can form, show on the screen what kind of triangle will be formed:
# Equilateral: all sides equal; Isosceles: two equal sides; Scalene: all different sides.

a = float(input('Length of first side: '))
b = float(input('Length of second side: '))
c = float(input('Length of Third side: '))

# cond = abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b
# if cond is True and a == b == c:
#     print('The above segments CAN FORM an EQUILATERAL triangle')
# elif cond is True and a == b != c or a != b == c or a == c != b:
#     print('The above segments CAN FORM an ISOSCELES triangle')
# elif cond is True and a != b != c != a:
#     print('The above segments CAN FORM an SCALENE triangle')
# else:
#     print('The above segments CANNOT FORM a triangle')

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('The above segments CAN FORM an Triangle,', end=' ')
    if a == b == c:
        print('An EQUILATERAL Triangle')
    elif a != b != c != a:
        print('An SCALENE Triangle')
    else:
        print('An ISOSCELES Triangle')
else:
    print('The above segments CANNOT FORM a Triangle')
