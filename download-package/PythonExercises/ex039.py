# Make a program that reads the year of birth of a young person and reports, according to their age:
# If he is still going to enlist in the military; If it's time to enlist; If you are past the time of enlistment.
# Your program should also show how much time is left or past the deadline.

from datetime import date

birth = int(input('Enter your year of birth: '))
year = date.today().year
age = year - birth
print('Whoever was born in {} is {} years ond in {}'.format(birth, age, year))
if age < 18:
    s = 18 - age
    print('Enlistment is still {} years away. \nYour enlistment will be in {}.'.format(s, year + s))
elif age > 18:
    s = age - 18
    print('You should have signed up {} years ago. \nYour enlistment was in {}'.format(s, year - s))
else:
    print('You have to enlist IMMEDIATELY.')
