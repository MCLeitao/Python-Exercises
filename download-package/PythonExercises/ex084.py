# Make a program that reads the names and weight of several people, keeping everything in a list. At the end, show:
# A)How many people were registered. B)A listing with the heaviest people. C)A listing with the lightest people.

data = list()
people = list()
heaviest = lightest = 0
while True:
    data.append(str(input('Name: ')))
    data.append(float(input('Weight: ')))
    if len(people) == 0:
        heaviest = lightest = data[1]
    else:
        if data[1] > heaviest:
            heaviest = data[1]
        elif data[1] < lightest:
            lightest = data[1]
    people.append(data[:])
    data.clear()
    choice = ' '
    while choice not in 'YN':
        choice = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if choice == 'N':
        break
"""
heaviest = lightest = people[0][1]
for weight in people:
    if weight[1] > heaviest:
        heaviest = weight[1]
    elif weight[1] < lightest:
        lightest = weight[1]
"""
print('-=' * 30)
print(f'Altogether, you registered {len(people)} people.')

print(f'The greatest weight was {heaviest:.1f}Kg. Weight of', end=' ')
for name in people:
    if name[1] == heaviest:
        print(f'[{name[0]}]', end='')
print('.')

print(f'The smallest weight was {lightest:.1f}Kg. Weight of', end=' ')
for name in people:
    if name[1] == lightest:
        print(f'[{name[0]}]', end='')
print('.')
