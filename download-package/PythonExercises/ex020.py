# The same teacher from the previous challenge wants to raffle off the order in which students present their work.
# Make a program that reads the names of the four students and shows the order drawn.

from random import shuffle

a = str(input('First student: '))
b = str(input('Second student: '))
c = str(input('Third student: '))
d = str(input('Fourth student: '))
# names = str(input('Type the students names: ')).strip()
list = [a, b, c, d]
shuffle(list)
# students = names.split()
# shuffle(students)
print('The order of presentation is: \n{}{}{}'.format('\033[1;30m', list, '\033[m'))
# print('The order of presentation is: {} '.format(students))
