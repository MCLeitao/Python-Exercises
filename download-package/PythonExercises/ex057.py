# Make a program that reads a person's gender, but only accepts the 'M' or 'F' values.
# If it is wrong, ask for the typing again until it has a correct value.
"""
sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Tell your gender: [M/F] ')).strip().upper()[0]
    if sex != 'M' and sex != 'F':
        print('\033[31mInvalid data\033[m')
print(f'Sex {sex} successfully registered.'
"""

# or:

sex = str(input('Tell your gender: [M/F] ')).strip().upper()[0]
while sex not in 'MF':
    sex = str(input('Invalid data. Please, tell your gender: ')).strip().upper()[0]
print(f'Sex {sex} successfully registered.')

# Start of data validation.
