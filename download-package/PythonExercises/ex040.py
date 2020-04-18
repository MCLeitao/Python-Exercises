# Create a program that reads 2 notes from a student and calculates their average, showing a message at the end,
# according to the average achieved:
# Average below 5.0: Fail; Average between 5.0 and 6.9: Recovery; Average 7.0 or higher: Approved.

n1 = float(input('Enter the First Note: '))
n2 = float(input('Enter the Second Note: '))
a = (n1 + n2) / 2
print('The AVERAGE is: {:.1f}'.format(a))
if a < 5:
    print('Student \033[1;30;41m Failed \033[m')
elif 5 <= a < 7:
    print('Student in \033[7;30m Recovery \033[m')
else:
    print('Student \033[1;30;42m Approved \033[m')
