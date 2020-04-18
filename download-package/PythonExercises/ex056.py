# Develop a program that reads the name, age and sex of four people. At the end of the program, show:
# The mean age of the group; What is the name of the oldest man; How many women are under twenty.

sa = 0
young = 0

print('-' * 20)
for ask in range(0, 4):
    name = str(input('Enter the name: '))
    age = int(input('Enter the age: '))
    sa += age
    sex = str(input('Enter the sex: '))
    if age < 20 and sex == 'female':
        young += 1
    print('-' * 20)
print('* The mean age of the group is: {} years'.format(sa / 4))
print('* {} women are under 20 years'.format(young))
