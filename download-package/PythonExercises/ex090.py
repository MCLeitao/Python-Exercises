# Make a program that reads a student's name and average, and also stores the situation in a dictionary.
# At the end, show the content of the structure on the screen.

student = dict()
student['Name'] = str(input('Name: '))
student['Average'] = float(input(f'{student["Name"]} average: '))
if student['Average'] >= 7:
    student['Situation'] = 'Approved'
elif 5 <= student['Average'] < 7:
    student['Situation'] = 'Recovery'
else:
    student['Situation'] = 'Disapproved'
print('-' * 20)
for key, value in student.items():
    print(f'{key} is equal to {value}')
print('-' * 20)
