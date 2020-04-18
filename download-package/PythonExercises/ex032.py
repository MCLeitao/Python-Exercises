# Make a program that reads any year and shows if it is a leap year (bissextile year).

from datetime import date

y = int(input('Enter a year. Type 0 to analyze the current year: '))
if y == 0:
    y = date.today().year
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('The year {} is a \033[1;32;47m leap year \033[m'.format(y))
else:
    print('The year {} is \033[1;30;41m NOT \033[m a leap year'.format(y))

# These extra days occur in each year which is an integer multiple of 4 (except for years evenly divisible by 100,
# which are not leap years unless evenly divisible by 400)
