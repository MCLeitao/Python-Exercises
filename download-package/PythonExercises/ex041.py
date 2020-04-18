# The National Swimming Confederation needs a program that reads the year of birth of an athlete and shows his category,
# according to age.
# Up to 9 years: Child; Up to 14 years: Infant; Up to 19 years: Junior; Up to 25 years: Senior; Above: Master

from datetime import date

birth = int(input('Enter the year of Birth: '))
age = date.today().year - birth
print('The athlete is {} years old'.format(age))
if age <= 9:
    print('Classification: \033[1;33;44m CHILD \033[m')
elif age <= 14:
    print('Classification: \033[1;35;43m INFANT \033[m')
elif age <= 19:
    print('Classification: \033[1;30;42m JUNIOR \033[m')
elif age <= 25:
    print('Classification: \033[1;30;41m SENIOR \033[m')
else:
    print('Classification: \033[1;7;30m MASTER \033[m')
