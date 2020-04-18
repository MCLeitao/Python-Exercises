# Create a program that reads the birth year of seven people.
# At the end, show how many people have not yet reached the age of majority (>= 21) and how many are of legal age.

from datetime import date
today = date.today().year
maj = 0
min = 0
for ask in range(0, 7):
    birth = int(input('Enter the Year of Birth: '))
    if today - birth >= 21:
        maj += 1
    else:
        min += 1
print('-' * 20)
print('{} people have reached adulthood'.format(maj))
print('{} people have NOT yet reached the age of majority'.format(min))
print('-' * 20)
