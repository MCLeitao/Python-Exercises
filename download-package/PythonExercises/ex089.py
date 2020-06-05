# Create a program that reads the name and two notes of several students and stores everything in a compound list.
# At the end, show a bulletin containing the average of each one and allow the user to show the grades of each student
# individually.

sheet = list()
while True:
    name = str(input('Name: '))
    note1 = float(input('Note 1: '))
    note2 = float(input('Note 2: '))
    average = (note1 + note2) / 2
    sheet.append([name, [note1, note2], average])
    choice = ' '
    while choice not in 'YN':
        choice = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if choice in 'N':
        break
print('-=' * 25)
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
print('-' * 22)
for index, student in enumerate(sheet):
    print(f'{index:<4}{student[0]:<10}{student[2]:>8.1f}')
print('-' * 22)
print('-=' * 25)
while True:
    choice = int(input('Show which student`s grades? (999 interrupts): '))
    if choice == 999:
        print('FINISHING...')
        break
    if choice <= len(sheet) - 1:
        print(f'{sheet[choice][0]}`s grades are {sheet[choice][1]}')
    print('-' * 50)
print('<<< WELCOME BACK >>>')
