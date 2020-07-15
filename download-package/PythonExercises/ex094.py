# Create a program that reads the name, sex and age of several people, saving each person's data in a dictionary and
# all dictionaries in a list. At the end, show:  A) How many people were registered; B) The average age of the group;
# C) A list of all women; D) A list of all above average people.

people = list()
person = dict()
sum = average = 0
# Reading the data:
while True:
    person['Name'] = str(input('Name: ')).title()
    while True:
        person['Gender'] = str(input('Gender: [M/F] ')).strip().upper()[0]
        if person['Gender'] in 'MF':
            break
        print('Error! Please enter only M or F.')
    person['Age'] = int(input('Age: '))
    sum += person['Age']
    people.append(person.copy())
    while True:
        choice = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
        if choice in 'YN':
            break
        print('Error! Please enter only Y or N.')
    if choice == 'N':
        break
print('-=' * 30)
# Analysis of the data entered:
print(f'A) Altogether we have {len(people)} people registered.')

'''
for person in people:
    sum += person['Age']
'''
average = sum / len(people)
print(f'B) The average age in {average:.2f} years old.')

print('C) The registered women were:', end=' ')
for person in people:
    if person['Gender'] == 'F':
        print(f'{person["Name"]}', end=' ')
print('.')

print('D) List of people who are above average:')
for person in people:
    if person['Age'] >= average:
        print('   ', end='')
        for key, value in person.items():
            print(f'{key} = {value}', end='; ')
        print()
print('<< Program Closed >>')
