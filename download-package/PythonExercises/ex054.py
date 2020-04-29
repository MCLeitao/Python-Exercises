# Create a program that reads the birth year of seven people.
# At the end, show how many people have not yet reached the age of majority (>= 21) and how many are of legal age.

from datetime import date
today = date.today().year
maj = 0
min = 0
for people in range(1, 8):
    birth = int(input(f'What year was the {people}ª person born? '))
    age = today - birth
    if age >= 21:
        maj += 1
    else:
        min += 1
print('-' * 20)
print(f'{maj} people have reached adulthood.')
print(f'{min} people have NOT yet reached the age of majority.')
print('-' * 20)
