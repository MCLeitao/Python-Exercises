# Write a program that asks the number of kilometers a car has driven and the number of days it has been hired.
# Calculate the price to pay, knowing that the car costs US$ 60 per day and US$ 0.15 per km driven.

k = float(input('Enter how many kilometers the car has traveled: '))
d = float(input('Enter how many days the car has been rented: '))
t = (k * 0.15) + (d * 60)
print('The total rental of the car is {}US${:.2f}{}'.format('\033[1;31;40m', t, '\033[m'))
