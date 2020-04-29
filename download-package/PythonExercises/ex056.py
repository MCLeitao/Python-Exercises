# Develop a program that reads the name, age and sex of four people. At the end of the program, show:
# The mean age of the group; What is the name of the oldest man; How many women are under twenty.

sum = 0
average = 0
older = 0
oldname = ''
young = 0
for reader in range(1, 5):
    print('----- {}ª Person -----'.format(reader))
    name = str(input('Name: ')).strip().title()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip()[0]
    sum += age
    if reader == 1 and sex in 'Mm':
        older = age
        oldname = name
    if sex in 'Mm' and age > older:
        older = age
        oldname = name
    if age < 20 and sex in 'Ff':
        young += 1
average = sum / 4
print(f'The mean age of the group is {average} years.')
print(f'The oldest man is {older} years old and is called {oldname}.')
print(f'There are {young} women under 20 years old.')
