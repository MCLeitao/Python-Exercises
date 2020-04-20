# Create a program that reads the birth year of seven people.
# At the end, show how many people have not yet reached the age of majority (>= 21) and how many are of legal age.

from datetime import date
today = date.today().year
maj = 0
min = 0
for people in range(1, 8):
    birth = int(input('What year was the {}ª person born? '.format(people)))
    age = today - birth
    if age >= 21:
        maj += 1
    else:
        min += 1
print('-' * 20)
print('{} people have reached adulthood'.format(maj))
print('{} people have NOT yet reached the age of majority'.format(min))
print('-' * 20)
