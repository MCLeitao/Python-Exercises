# Create a program that reads the age and sex of several people. For each registered person, the program should ask if
# the user wants to continue or not. At the end, it shows:
# A) How many people are over 18 years old. B) How many men were registered. C) How many women are under 20 years old.

over18 = men = under20 = 0
while True:
    print('-' * 25)
    print('{:^25}'.format('REGISTER A PERSON'))
    print('-' * 25)
    age = int(input('Age: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sex: [M/F] ')).strip().upper()[0]
    if age >= 18:
        over18 += 1
    if sex == 'M':
        men += 1
    if sex == 'F' and age < 20:
        under20 += 1
    print(('-' * 25))
    proceed = ' '
    while proceed not in 'YN':
        proceed = str(input('Want to continue? [Y/N] ')).strip().upper()[0]
    if proceed == 'N':
        break
print('{:=^30}'.format(' END OF PROGRAM '))
print(f'Total of people over 18 years old: {over18}')
print(f'In all we have {men} men registered.')
print(f'We have {under20} women under 20 years old.')
