# Create a program that reads name, year of birth and work permit and records them (with age) in a dictionary, if by
# chance the National Insurance Number (NI number) is different from zero, the dictionary will also receive the year of
# hire and salary. Calculate and add, in addition to age, how old the person will retire (35 years of contribution).

from datetime import date
# from datetime import datetime

data = dict()

data['Name'] = str(input('Name: '))
year_birth = int(input('Year of Birth: '))
data['Age'] = date.today().year - year_birth  # datetime.now().year - year_birth
data['Work Permit'] = int(input('Work Permit (0 there is not): '))
if data['Work Permit'] != 0:
    data['Hire'] = int(input('Year of Hide: '))
    data['Salary'] = float(input('Salary: US$ '))
    data['Retire'] = data['Age'] + ((data['Hire'] + 35) - date.today().year)

print('--' * 15)
for key, value in data.items():
    print(f'* {key} is worth {value}')
