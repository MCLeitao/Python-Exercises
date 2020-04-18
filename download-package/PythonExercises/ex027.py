# Make a program that reads a person's full name, then shows the first and last names separately.

name = str(input('Type your full name: ')).strip().title().split()
print('First name is: {}{}{}\nLast name is: {}{}{}'.format('\033[1;31;40m', name[0], '\033[m', '\033[1;30;41m',
                                                           name[len(name) - 1], '\033[m'))
