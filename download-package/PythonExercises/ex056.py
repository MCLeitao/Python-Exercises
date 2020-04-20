# Develop a program that reads the name, age and sex of four people. At the end of the program, show:
# The mean age of the group; What is the name of the oldest man; How many women are under twenty.

sum = 0
average = 0
older = 0
oldname = ''
young = 0
for p in range(1, 5):
    print('----- {}ª Person -----'.format(p))
    name = str(input('Name: ')).strip().title()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).strip()
    sum += age
    if p == 1 and sex in 'Mm':
        older = age
        oldname = name
    if sex in 'Mm' and age > older:
        older = age
        oldname = name
    if age < 20 and sex in 'Ff':
        young += 1
average = sum / 4
print('The mean age of the group is {} years.'.format(average))
print('The oldest man is {} years old and is called {}.'.format(older, oldname))
print('There are {} women under 20 years old'.format(young))
