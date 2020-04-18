# A teacher wants draw one of his four students to erase the board.
# Make a program that helps him, reading their name and writing the name of the chosen one.

from random import choice

a = str(input('Type the First student: '))
b = str(input('Type the Second student: '))
c = str(input('Type the Third student: '))
d = str(input('Type the Fourth student: '))
# names = str(input('Enter the name of the students: ')).strip()
students = [a, b, c, d]
# students = names.split()
print('The chosen student was {}{}{} !'.format('\033[1;31;40m', choice(students), '\033[m'))
